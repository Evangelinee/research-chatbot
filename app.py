"""
Research Chatbot - Conversational Interface
A Streamlit app that chats naturally with users about research papers
"""

import streamlit as st
import hashlib
from backend.pdf_processor import process_pdf_file
from backend.vector_store import VectorStore
from backend.intent_handler import IntentHandler
from frontend.styles import apply_custom_css, display_sidebar_status
from backend.config import MAX_PAPERS
from utils.helpers import extract_source_files
import time


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
        st.session_state.selected_intent = None
    
    if "papers_loaded" not in st.session_state:
        st.session_state.papers_loaded = False
    
    if "paper_filenames" not in st.session_state:
        st.session_state.paper_filenames = []
    
    if "conversation_started" not in st.session_state:
        st.session_state.conversation_started = False
    
    if "waiting_for_intent" not in st.session_state:
        st.session_state.waiting_for_intent = False


# Process uploaded papers
def process_uploaded_papers(uploaded_files):
    """Process and index uploaded PDF files."""
    
    all_chunks = []
    all_metadata = {}
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i, file in enumerate(uploaded_files[:MAX_PAPERS]):
        status_text.markdown(f"**Processing:** {file.name}")
        
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
    status_text.markdown("**Building search index...**")
    st.session_state.vector_store.create_index(all_chunks)
    st.session_state.chunk_metadata = all_metadata
    st.session_state.paper_filenames = [f.name for f in uploaded_files[:MAX_PAPERS]]
    st.session_state.papers_loaded = True
    
    status_text.markdown("**Processing complete!**")
    
    return len(uploaded_files[:MAX_PAPERS]), len(all_chunks)


def start_conversation():
    """Start the conversation with welcome message and intent options"""
    
    welcome_message = """Hello! I'm your Research Assistant. I can help you analyze your research papers in different ways.

**How would you like me to help you today? Please choose an option:**

1. **Fact Finding** - Get factual information and specific details from your papers
2. **Research Gaps** - Identify limitations, gaps, and opportunities for future research
3. **Hypothesis Generation** - Generate new hypotheses based on the research
4. **Contradiction Detection** - Find conflicting findings or disagreements between papers
5. **General Discussion** - Have a general conversation about your research papers

You can type the number (1-5) or the name of the intent."""
    
    st.session_state.messages.append({"role": "assistant", "content": welcome_message})
    st.session_state.conversation_started = True
    st.session_state.waiting_for_intent = True


def set_intent_from_user_input(user_input):
    """Parse user input to determine intent"""
    
    user_input_lower = user_input.lower().strip()
    
    # Map user input to intent
    intent_map = {
        "1": "fact",
        "fact": "fact",
        "fact finding": "fact",
        "get facts": "fact",
        "factual": "fact",
        "2": "gap",
        "gap": "gap",
        "research gaps": "gap",
        "gaps": "gap",
        "limitations": "gap",
        "3": "hypothesis",
        "hypothesis": "hypothesis",
        "generate hypothesis": "hypothesis",
        "hypotheses": "hypothesis",
        "4": "contradiction",
        "contradiction": "contradiction",
        "contradictions": "contradiction",
        "conflicts": "contradiction",
        "conflicting": "contradiction",
        "5": "general",
        "general": "general",
        "general discussion": "general",
        "chat": "general",
        "talk": "general"
    }
    
    return intent_map.get(user_input_lower, None)


def get_intent_confirmation_message(intent):
    """Get confirmation message for selected intent"""
    
    messages = {
        "fact": "Great! I'll help you find **factual information** from your research papers. You can now ask me specific questions about the content, methodologies, results, or any other factual details. What would you like to know?",
        "gap": "Excellent! I'll help you identify **research gaps and limitations**. Ask me about unexplored areas, methodological weaknesses, or opportunities for future research. What specific area would you like to explore?",
        "hypothesis": "Interesting! I'll help **generate new hypotheses** based on your research papers. Share your observations or ask about potential relationships that could be investigated further. What would you like to hypothesize about?",
        "contradiction": "Good choice! I'll help **find contradictions and conflicting findings** across your papers. Ask me about disagreements, inconsistent results, or varying conclusions. What topic would you like me to analyze?",
        "general": "Perfect! I'm ready for a **general discussion** about your research papers. Feel free to ask any questions, share thoughts, or explore ideas. What's on your mind?"
    }
    
    return messages.get(intent, f"I'll help you with {intent} intent. What would you like to know?")


# Main app
def main():
    """Main application entry point."""
    
    # Page config
    st.set_page_config(
        page_title="Research Chatbot - Conversational AI Assistant",
        page_icon="📚",
        layout="wide"
    )
    
    # Apply custom CSS
    apply_custom_css()
    
    # Initialize session state
    init_session_state()
    
    # Title section
    st.markdown('<div class="main-title">Research Assistant</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Conversational AI for research paper analysis</div>', unsafe_allow_html=True)
    
    # Sidebar - Configuration
    with st.sidebar:
        st.markdown("## Configuration")
        
        # API Key input
        api_key = st.text_input(
            "Groq API Key", 
            type="password",
            placeholder="Enter your Groq API key",
            help="Get a free API key from console.groq.com",
            key="groq_api_key_input"
        )
        
        if api_key:
            try:
                # Use a current model - llama3-70b-8192 or mixtral-8x7b-32768
                st.session_state.intent_handler = IntentHandler(api_key, model="mixtral-8x7b-32768")
                st.success("API key configured")
            except Exception as e:
                st.error(f"Error: {str(e)}")
        
        # Display status
        display_sidebar_status(
            st.session_state.papers_loaded,
            len(st.session_state.paper_filenames),
            len(st.session_state.vector_store.chunks) if st.session_state.vector_store else 0
        )
        
        # Clear button
        if st.session_state.papers_loaded:
            st.markdown("---")
            if st.button("Clear All", use_container_width=True):
                st.session_state.vector_store.clear()
                st.session_state.chunk_metadata = {}
                st.session_state.messages = []
                st.session_state.papers_loaded = False
                st.session_state.conversation_started = False
                st.session_state.waiting_for_intent = False
                st.session_state.selected_intent = None
                st.rerun()
    
    # Main content area - Papers Upload
    if not st.session_state.papers_loaded:
        st.markdown("### Upload Research Papers")
        st.markdown("Please upload your research papers (PDF format) ")
        
        uploaded_files = st.file_uploader(
            "Choose PDF files",
            type="pdf",
            accept_multiple_files=True,
            help="Upload up to 5 research papers in PDF format",
            key="main_uploader"
        )
        
        if uploaded_files:
            if len(uploaded_files) > MAX_PAPERS:
                st.warning(f"Only the first {MAX_PAPERS} papers will be processed")
            
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("Process Papers", type="primary", use_container_width=True):
                    if not api_key:
                        st.error("Please enter your Groq API key in the sidebar first")
                    elif not st.session_state.intent_handler:
                        st.error("API key not configured properly")
                    else:
                        with st.spinner("Processing papers..."):
                            num_papers, num_chunks = process_uploaded_papers(uploaded_files)
                            st.success(f"Processed {num_papers} papers, {num_chunks} chunks")
                            # Start the conversation after papers are loaded
                            start_conversation()
                            st.rerun()
        
        # Show instructions if no papers uploaded
        if not uploaded_files:
            st.info("📄 Upload PDF files to get started. The assistant will guide you through the conversation.")
        
        st.stop()
    
    # Chat interface (shown when papers are loaded)
    
    # Check if intent handler is ready
    if not st.session_state.intent_handler:
        st.warning("Please configure your Groq API key in the sidebar to continue")
        st.stop()
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
            if "sources" in message and message["sources"]:
                with st.expander("View Sources"):
                    for source in message["sources"]:
                        st.caption(f"- {source}")
    
    # Chat input
    user_input = st.chat_input("Type your message here...")
    
    if user_input:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Process based on conversation state
        with st.chat_message("assistant"):
            if st.session_state.waiting_for_intent:
                # User is selecting intent
                intent = set_intent_from_user_input(user_input)
                
                if intent:
                    st.session_state.selected_intent = intent
                    st.session_state.waiting_for_intent = False
                    
                    # Send confirmation message
                    confirmation = get_intent_confirmation_message(intent)
                    st.markdown(confirmation)
                    
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": confirmation
                    })
                else:
                    # Invalid intent selection
                    error_msg = """I didn't recognize that intent. Please choose from:

**1. Fact Finding** - Get factual information
**2. Research Gaps** - Identify limitations and gaps
**3. Hypothesis Generation** - Generate new hypotheses
**4. Contradiction Detection** - Find conflicting findings
**5. General Discussion** - General conversation

Please type the number (1-5) or the name of the intent."""
                    
                    st.markdown(error_msg)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": error_msg
                    })
            
            else:
                # Normal conversation - process the question with selected intent
                with st.spinner(f"Analyzing with {st.session_state.selected_intent} intent..."):
                    
                    # Search for relevant chunks
                    relevant_chunks = st.session_state.vector_store.search(
                        user_input, 
                        k=4
                    )
                    
                    if not relevant_chunks:
                        response = "I couldn't find relevant information in the uploaded papers. Could you please rephrase your question or ask about a different topic?"
                    else:
                        # Generate response with error handling for model issues
                        try:
                            response = st.session_state.intent_handler.generate_response(
                                question=user_input,
                                context_chunks=relevant_chunks,
                                intent=st.session_state.selected_intent,
                                chat_history=st.session_state.messages[:-1]
                            )
                        except Exception as e:
                            if "model_decommissioned" in str(e):
                                response = "I need to update my model configuration. Please try asking your question again."
                                # Try to reinitialize with a different model
                                try:
                                    api_key = st.session_state.intent_handler.api_key
                                    st.session_state.intent_handler = IntentHandler(api_key, model="mixtral-8x7b-32768")
                                    response = st.session_state.intent_handler.generate_response(
                                        question=user_input,
                                        context_chunks=relevant_chunks,
                                        intent=st.session_state.selected_intent,
                                        chat_history=st.session_state.messages[:-1]
                                    )
                                except:
                                    response = "I'm experiencing technical difficulties. Please check your API key and try again."
                            else:
                                response = f"I encountered an error: {str(e)}. Please try again."
                    
                    st.markdown(response)
                    
                    # Extract and display sources
                    sources = extract_source_files(relevant_chunks, st.session_state.chunk_metadata)
                    
                    if sources and not relevant_chunks:
                        with st.expander("Sources Used"):
                            for source in set(sources):
                                st.caption(f"- {source}")
        
        # Add assistant response to history
        if not st.session_state.waiting_for_intent:
            st.session_state.messages.append({
                "role": "assistant",
                "content": response,
                "sources": list(set(sources)) if sources else []
            })
        
        st.rerun()
    
    # If conversation hasn't started yet, start it
    if not st.session_state.conversation_started and st.session_state.papers_loaded:
        start_conversation()
        st.rerun()


if __name__ == "__main__":
    main()