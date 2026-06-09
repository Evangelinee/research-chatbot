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