"""
Frontend styling module: CSS and UI components for Streamlit.
"""

import streamlit as st
from backend.config import INTENT_COLORS, INTENT_DESCRIPTIONS


def apply_custom_css():
    """Apply custom CSS styling to the Streamlit app."""
    
    st.markdown("""
    <style>
        /* Main app background */
        .stApp {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        }
        
        /* Headers */
        h1, h2, h3 {
            color: white !important;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        /* Main title */
        .main-title {
            text-align: center;
            background: linear-gradient(120deg, #ffffff, #e0c3fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 1rem;
        }
        
        /* Chat messages */
        .user-message {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1rem;
            border-radius: 1rem;
            margin-bottom: 1rem;
        }
        
        .assistant-message {
            background: rgba(255,255,255,0.95);
            color: #1e3c72;
            padding: 1rem;
            border-radius: 1rem;
            margin-bottom: 1rem;
            border-left: 5px solid #00b4d8;
        }
        
        /* Buttons */
        .stButton > button {
            border-radius: 20px;
            padding: 8px 20px;
            transition: all 0.3s ease;
            font-weight: 600;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        /* Intent selector */
        .intent-container {
            display: flex;
            gap: 10px;
            margin: 20px 0;
        }
        
        .selected-intent {
            padding: 10px;
            border-radius: 10px;
            margin: 10px 0;
            text-align: center;
            font-weight: bold;
        }
        
        /* Sidebar */
        .css-1d391kg {
            background: rgba(255,255,255,0.95);
        }
        
        /* Info boxes */
        .info-box {
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
            padding: 1rem;
            margin: 1rem 0;
        }
        
        /* Status indicators */
        .status-success {
            color: #4CAF50;
            font-weight: bold;
        }
        
        .status-warning {
            color: #FF9800;
            font-weight: bold;
        }
        
        .status-error {
            color: #F44336;
            font-weight: bold;
        }
        
        /* Expander styling */
        .streamlit-expanderHeader {
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
        }
        
        /* Code blocks */
        code {
            background: #1e1e1e;
            color: #d4d4d4;
            padding: 2px 5px;
            border-radius: 5px;
        }
    </style>
    """, unsafe_allow_html=True)


def display_intent_selector(current_intent: str):
    """
    Display clickable intent selection buttons.
    
    Args:
        current_intent: Currently selected intent
        
    Returns:
        Newly selected intent (if changed)
    """
    
    st.markdown("### Select your question type:")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # Define button labels and their corresponding intents
    buttons = [
        (col1, "Fact", "fact"),
        (col2, "Gap", "gap"),
        (col3, "Hypothesis", "hypothesis"),
        (col4, "Contradiction", "contradiction"),
        (col5, "General", "general")
    ]
    
    selected = current_intent
    
    for col, label, intent in buttons:
        # Style button based on selection
        button_style = "primary" if current_intent == intent else "secondary"
        
        if col.button(label, key=f"intent_{intent}", use_container_width=True):
            selected = intent
    
    # Display current selection
    color = INTENT_COLORS.get(selected, "#2196F3")
    description = INTENT_DESCRIPTIONS.get(selected, "General conversation")
    
    st.markdown(f"""
    <div class="selected-intent" style="background-color: {color}20; border-left: 5px solid {color};">
        Current intent: <strong>{selected.upper()}</strong>
        <span style="font-size: 0.8rem;">
            ({description})
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    return selected


def display_chat_message(role: str, content: str):
    """
    Display a single chat message with proper styling.
    
    Args:
        role: Either "user" or "assistant"
        content: Message content
    """
    
    if role == "user":
        st.markdown(f'<div class="user-message">{content}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="assistant-message">{content}</div>', unsafe_allow_html=True)


def display_welcome_message():
    """Display the welcome message when no papers are loaded."""
    
    st.markdown("""
    <div class="info-box">
        <h3>Welcome to Research Chatbot</h3>
        <p><strong>Get started:</strong></p>
        <ol>
            <li>Enter your Groq API key in the sidebar</li>
            <li>Upload up to 5 research papers (PDF format)</li>
            <li>Click "Process Papers" to index them</li>
            <li>Select your question type (Fact, Gap, Hypothesis, Contradiction, or General)</li>
            <li>Ask questions about your papers</li>
        </ol>
        <p><em>The chatbot will retrieve relevant information and respond based on your selected intent.</em></p>
    </div>
    """, unsafe_allow_html=True)


def display_sidebar_status(has_papers: bool, paper_count: int = 0, chunk_count: int = 0):
    """
    Display status information in the sidebar.
    
    Args:
        has_papers: Whether papers are loaded
        paper_count: Number of papers loaded
        chunk_count: Number of text chunks indexed
    """
    
    st.markdown("---")
    st.markdown("### Status")
    
    if has_papers:
        st.markdown(f'<span class="status-success">Papers loaded: {paper_count}</span>', unsafe_allow_html=True)
        st.markdown(f'<span class="status-success">Chunks indexed: {chunk_count}</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="status-warning">No papers loaded</span>', unsafe_allow_html=True)
        st.markdown("Upload PDFs using the button above.")