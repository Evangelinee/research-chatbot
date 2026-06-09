<<<<<<< HEAD
"""
Professional UI Styling for Research Chatbot
"""

import streamlit as st

def apply_custom_css():
    """Apply clean, professional CSS styling without emojis"""
    
    st.markdown("""
    <style>
    /* Import professional fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global styles */
    .stApp {
        background: #f5f7fa;
        font-family: 'Inter', sans-serif;
    }
    
    /* Main container */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Title styling */
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1a1a2e;
        margin-bottom: 0.25rem;
        letter-spacing: -0.02em;
    }
    
    /* Subtitle */
    .subtitle {
        font-size: 1rem;
        color: #666;
        margin-bottom: 2rem;
        font-weight: 400;
        border-bottom: 2px solid #e0e0e0;
        padding-bottom: 1rem;
    }
    
    /* Welcome message styling */
    .welcome-container {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        border: 1px solid #e0e0e0;
    }
    
    .welcome-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1a1a2e;
        margin-bottom: 1.5rem;
        border-left: 4px solid #4a90e2;
        padding-left: 1rem;
    }
    
    .step-list {
        margin: 1.5rem 0;
    }
    
    .step-item {
        padding: 0.75rem 0;
        color: #444;
        font-size: 0.95rem;
        border-bottom: 1px solid #f0f0f0;
    }
    
    .step-number {
        display: inline-block;
        width: 28px;
        height: 28px;
        background: #4a90e2;
        color: white;
        border-radius: 6px;
        text-align: center;
        line-height: 28px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 0.75rem;
    }
    
    /* Upload section styling */
    .upload-section {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        border: 2px dashed #cbd5e1;
    }
    
    .section-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #1a1a2e;
        margin-bottom: 1rem;
    }
    
    /* Chat message styling */
    [data-testid="stChatMessage"] {
        background: transparent;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    
    [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] {
        font-size: 0.95rem;
        line-height: 1.6;
        color: #333;
    }
    
    /* User message styling */
    [data-testid="stChatMessage"]:nth-child(odd) {
        background: #f0f4f8;
        border-left: 3px solid #4a90e2;
    }
    
    /* Assistant message styling */
    [data-testid="stChatMessage"]:nth-child(even) {
        background: white;
        border: 1px solid #e0e0e0;
        border-left: 3px solid #2c3e50;
    }
    
    /* Button styling */
    .stButton > button {
        background: #4a90e2;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1.2rem;
        font-weight: 500;
        font-size: 0.9rem;
        transition: all 0.2s ease;
    }
    
    .stButton > button:hover {
        background: #357abd;
        transform: translateY(-1px);
        box-shadow: 0 2px 8px rgba(74, 144, 226, 0.3);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: white;
        border-right: 1px solid #e0e0e0;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: #333;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #1a1a2e;
        font-weight: 600;
    }
    
    /* Sidebar input styling */
    [data-testid="stSidebar"] .stTextInput > div > div > input {
        background: white;
        border: 1px solid #cbd5e1;
        color: #333;
        border-radius: 6px;
    }
    
    [data-testid="stSidebar"] .stTextInput > div > div > input:focus {
        border-color: #4a90e2;
        box-shadow: 0 0 0 2px rgba(74, 144, 226, 0.1);
    }
    
    /* File uploader styling */
    [data-testid="stFileUploader"] {
        background: white;
        border: 2px dashed #cbd5e1;
        border-radius: 8px;
        padding: 1rem;
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: #4a90e2;
    }
    
    /* Success/Error messages */
    .stSuccess {
        background: #d4edda;
        color: #155724;
        border-radius: 6px;
        padding: 0.75rem;
        border-left: 3px solid #28a745;
    }
    
    .stError {
        background: #f8d7da;
        color: #721c24;
        border-radius: 6px;
        padding: 0.75rem;
        border-left: 3px solid #dc3545;
    }
    
    .stWarning {
        background: #fff3cd;
        color: #856404;
        border-radius: 6px;
        padding: 0.75rem;
        border-left: 3px solid #ffc107;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: #f8f9fa;
        border-radius: 6px;
        font-weight: 500;
        color: #4a90e2;
        border: 1px solid #e0e0e0;
    }
    
    /* Spinner styling */
    .stSpinner > div {
        border-top-color: #4a90e2 !important;
    }
    
    /* Status box styling */
    .status-box {
        background: #f8f9fa;
        border-radius: 8px;
        padding: 1rem;
        margin-top: 1rem;
        border: 1px solid #e0e0e0;
    }
    
    /* Info box styling */
    .info-box {
        background: #e8f0fe;
        color: #1a1a2e;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 3px solid #4a90e2;
    }
    
    /* Divider */
    hr {
        margin: 1.5rem 0;
        border: none;
        border-top: 2px solid #e0e0e0;
    }
    
    /* Progress bar */
    .stProgress > div > div > div > div {
        background: #4a90e2;
    }
    
    /* Select box styling */
    [data-testid="stSelectbox"] label {
        color: #1a1a2e;
        font-weight: 500;
        font-size: 0.9rem;
    }
    
    [data-testid="stSelectbox"] div {
        border-radius: 6px;
    }
    </style>
    """, unsafe_allow_html=True)


def display_intent_selector(selected_intent):
    """Display professional intent selector"""
    
    intent_options = {
        "fact": "Fact - Get factual information from papers",
        "gap": "Gap - Identify research gaps and opportunities",
        "hypothesis": "Hypothesis - Generate research hypotheses",
        "contradiction": "Contradiction - Find conflicting findings",
        "general": "General - General discussion and questions"
    }
    
    selected = st.selectbox(
        "Select Question Intent",
        options=list(intent_options.keys()),
        format_func=lambda x: intent_options[x],
        index=list(intent_options.keys()).index(selected_intent) if selected_intent in intent_options else 0,
        key="intent_selector"
    )
    
    return selected


def display_welcome_message():
    """Display clean welcome message without emojis"""
    
    st.markdown("""
    <div class="welcome-container">
        <div class="welcome-title">
            Get Started
        </div>
        <div class="step-list">
            <div class="step-item">
                <span class="step-number">1</span>
                <strong>Enter Groq API Key</strong> - Add your API key in the sidebar
            </div>
            <div class="step-item">
                <span class="step-number">2</span>
                <strong>Upload Research Papers</strong> - Add PDF files in the upload section below
            </div>
            <div class="step-item">
                <span class="step-number">3</span>
                <strong>Process Papers</strong> - Click the process button to index your documents
            </div>
            <div class="step-item">
                <span class="step-number">4</span>
                <strong>Select Intent</strong> - Choose the type of response you want
            </div>
            <div class="step-item">
                <span class="step-number">5</span>
                <strong>Ask Questions</strong> - Start chatting with your research papers
            </div>
        </div>
        <div class="info-box">
            <strong>Note:</strong> The chatbot will retrieve relevant information from your uploaded papers and respond based on your selected intent type.
        </div>
    </div>
    """, unsafe_allow_html=True)


def display_upload_section():
    """Display upload section in main page"""
    
    st.markdown("""
    <div class="upload-section">
        <div class="section-title">Upload Research Papers</div>
    </div>
    """, unsafe_allow_html=True)


def display_sidebar_status(papers_loaded, num_papers, num_chunks):
    """Display professional sidebar status"""
    
    st.markdown("---")
    st.markdown("### Status")
    
    if papers_loaded:
        st.markdown(f"""
        <div class="status-box">
            <strong>Papers Loaded:</strong> {num_papers}<br>
            <strong>Chunks Indexed:</strong> {num_chunks}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="status-box">
            <strong>Status:</strong> No papers loaded<br>
            <span style="font-size: 0.85rem; color: #666;">Upload papers in the main area to get started</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Add information section
    st.markdown("---")
    st.markdown("### Information")
    st.markdown("""
    **Supported formats:** PDF
    
    **Maximum files:** 5 papers
    
    **File size limit:** 200MB per file
    """)
=======
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
>>>>>>> 951aa9ade50f4641f91bcc6c951681eef93dc5b0
