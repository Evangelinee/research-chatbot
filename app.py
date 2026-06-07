"""
Research Chatbot - Main Application Entry Point
A Streamlit app that allows users to chat with research papers using intent-based responses.
"""

import streamlit as st
import hashlib
from backend.pdf_processor import process_pdf_file
from backend.vector_store import VectorStore
from backend.intent_handler import IntentHandler
from frontend.styles import (
    apply_custom_css, 
    display_intent_selector, 
    display_welcome_message,
    display_sidebar_status
)
from backend.config import MAX_PAPERS, INTENT_TYPES
from utils.helpers import extract_source_files


# Initialize session state
def init_session_state():
    """Initialize all session state variables."""
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = VectorStore()
    
    if "chunk_metadata" not in st.session_state:
        st.session_state.chunk_metadata = {}
    
    if "intent_handler" not in st.session_state:
        st.session_state.intent_handler = None
    
    if "selected_intent" not in st.session_state:
        st.session_state.selected_intent = "fact"
    
    if "papers_loaded" not in st.session_state:
        st.session_state.papers_loaded = False
    
    if "paper_filenames" not in st.session_state:
        st.session_state.paper_filenames = []


# Process uploaded papers
def process_uploaded_papers(uploaded_files):
    """Process and index uploaded PDF files."""
    
    all_chunks = []
    all_metadata = {}
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i, file in enumerate(uploaded_files[:MAX_PAPERS]):
        status_text.text(f"Processing {file.name}...")
        
        # Process PDF
        chunks, metadata = process_pdf_file(file)
        all_chunks.extend(chunks)
        
        # Store metadata for each chunk
        for chunk in chunks:
            chunk_id = hashlib.md5(chunk.encode()).hexdigest()
            all_metadata[chunk] = {
                "filename": file.name,
                "chunk_id": chunk_id,
                "paper_index": i
            }
        
        progress_bar.progress((i + 1) / len(uploaded_files[:MAX_PAPERS]))
    
    # Create vector store
    status_text.text("Building search index...")
    st.session_state.vector_store.create_index(all_chunks)
    st.session_state.chunk_metadata = all_metadata
    st.session_state.paper_filenames = [f.name for f in uploaded_files[:MAX_PAPERS]]
    st.session_state.papers_loaded = True
    
    status_text.text("Done!")
    
    return len(uploaded_files[:MAX_PAPERS]), len(all_chunks)


# Main app
def main():
    """Main application entry point."""
    
    # Page config
    st.set_page_config(
        page_title="Research Chatbot",
        page_icon="📚",
        layout="wide"
    )
    
    # Apply custom CSS
    apply_custom_css()
    
    # Initialize session state
    init_session_state()
    
    # Title
    st.markdown('<div class="main-title">Research Chatbot</div>', unsafe_allow_html=True)
    st.markdown("*Chat with your papers using intent-based responses*")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.markdown("## Setup")
        
        # API Key input
        api_key = st.text_input(
            "Groq API Key", 
            type="password",
            help="Get a free API key from console.groq.com"
        )
        
        if api_key:
            st.session_state.intent_handler = IntentHandler(api_key)
            st.success("API key configured")
        
        st.markdown("---")
        st.markdown("## Upload Papers")
        st.caption(f"Maximum {MAX_PAPERS} papers")
        
        uploaded_files = st.file_uploader(
            "Choose PDF files",
            type="pdf",
            accept_multiple_files=True,
            help="Upload research papers in PDF format"
        )
        
        if uploaded_files:
            if len(uploaded_files) > MAX_PAPERS:
                st.warning(f"Only first {MAX_PAPERS} papers will be processed")
            
            if st.button("Process Papers", type="primary", use_container_width=True):
                if not api_key:
                    st.error("Please enter your Groq API key first")
                else:
                    with st.spinner("Processing papers..."):
                        num_papers, num_chunks = process_uploaded_papers(uploaded_files)
                        st.success(f"Processed {num_papers} papers, {num_chunks} chunks")
                        st.rerun()
        
        # Display status
        display_sidebar_status(
            st.session_state.papers_loaded,
            len(st.session_state.paper_filenames),
            len(st.session_state.vector_store.chunks) if st.session_state.vector_store else 0
        )
        
        # Clear button
        if st.session_state.papers_loaded:
            if st.button("Clear All Papers", use_container_width=True):
                st.session_state.vector_store.clear()
                st.session_state.chunk_metadata = {}
                st.session_state.messages = []
                st.session_state.papers_loaded = False
                st.session_state.paper_filenames = []
                st.rerun()
    
    # Main chat area
    if not st.session_state.papers_loaded:
        display_welcome_message()
        st.stop()
    
    # Intent selector
    st.session_state.selected_intent = display_intent_selector(
        st.session_state.selected_intent
    )
    
    st.markdown("---")
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
            if "sources" in message and message["sources"]:
                with st.expander("Sources"):
                    for source in message["sources"]:
                        st.caption(f"- {source}")
    
    # Chat input
    question = st.chat_input("Ask a question about your research papers...")
    
    if question:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": question})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(question)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner(f"Analyzing with {st.session_state.selected_intent} intent..."):
                
                # Search for relevant chunks
                relevant_chunks = st.session_state.vector_store.search(
                    question, 
                    k=4
                )
                
                # Generate response
                response = st.session_state.intent_handler.generate_response(
                    question=question,
                    context_chunks=relevant_chunks,
                    intent=st.session_state.selected_intent,
                    chat_history=st.session_state.messages[:-1]
                )
                
                st.markdown(response)
                
                # Extract and display sources
                sources = extract_source_files(relevant_chunks, st.session_state.chunk_metadata)
                
                if sources:
                    with st.expander("Sources used"):
                        for source in set(sources):
                            st.caption(f"- {source}")
        
        # Add assistant response to history
        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "sources": list(set(sources)) if sources else []
        })
        
        st.rerun()


if __name__ == "__main__":
    main()