<<<<<<< HEAD
"""
Configuration settings for Research Chatbot
"""

# Maximum number of papers to process
MAX_PAPERS = 5

# Available Groq models (updated - removed deprecated llama3-8b-8192)
AVAILABLE_MODELS = [
    "mixtral-8x7b-32768",
    "llama3-70b-8192", 
    "gemma2-9b-it",
    "llama-3.1-8b-instant",
    "llama-3.2-1b-preview",
    "llama-3.2-3b-preview"
]

# Default model
DEFAULT_MODEL = "mixtral-8x7b-32768"

# Intent types
INTENT_TYPES = ["fact", "gap", "hypothesis", "contradiction", "general"]

# Embedding model configuration
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"  # Sentence transformer model for embeddings
EMBEDDING_DIMENSION = 384  # Dimension for all-MiniLM-L6-v2

# Vector store configuration
VECTOR_STORE_TYPE = "faiss"  # Using FAISS for similarity search
SIMILARITY_TOP_K = 4  # Number of similar chunks to retrieve

# Chunk configuration for PDF processing
CHUNK_SIZE = 1000  # Size of text chunks in characters
CHUNK_OVERLAP = 200  # Overlap between chunks to maintain context

# File upload configuration
MAX_FILE_SIZE_MB = 200
ALLOWED_EXTENSIONS = ["pdf"]

# System prompts for different intents
INTENT_PROMPTS = {
    "fact": """You are a research assistant focused on providing accurate, factual information from research papers. 
    Your responses should:
    - Be precise and evidence-based
    - Cite specific information from the provided context
    - Distinguish between stated facts and interpretations
    - Use direct quotes when relevant
    - Maintain academic rigor and objectivity""",
    
    "gap": """You are a research analyst identifying gaps and limitations in research papers.
    Your responses should:
    - Identify unexplored areas and methodological weaknesses
    - Suggest potential research directions
    - Critically evaluate the scope and limitations of the papers
    - Highlight contradictions or inconsistencies in findings
    - Propose specific questions that remain unanswered""",
    
    "hypothesis": """You are a research hypothesis generator based on existing literature.
    Your responses should:
    - Generate novel, testable hypotheses from the research context
    - Clearly state assumptions and expected relationships
    - Suggest specific variables and potential methodologies
    - Build logically from the presented evidence
    - Explain the theoretical rationale for each hypothesis""",
    
    "contradiction": """You are a research critic focusing on contradictions and conflicts in research.
    Your responses should:
    - Identify conflicting findings across different papers
    - Analyze methodological differences that might explain contradictions
    - Discuss varying theoretical perspectives
    - Evaluate the strength of conflicting evidence
    - Suggest ways to resolve apparent contradictions""",
    
    "general": """You are a helpful research assistant discussing academic papers.
    Your responses should:
    - Be conversational but professional
    - Provide clear explanations of complex concepts
    - Connect ideas across different papers when relevant
    - Ask clarifying questions when needed
    - Maintain an engaging and supportive tone"""
=======
"""
Configuration file for the Research Chatbot.
Contains constants, model names, and default settings.
"""

# Model configurations
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
LLM_MODEL_NAME = "llama3-8b-8192"

# Text processing
DEFAULT_CHUNK_SIZE = 500
DEFAULT_CHUNK_OVERLAP = 50
MAX_PAPERS = 5
MAX_CHUNKS_PER_PAPER = 100

# Search
DEFAULT_SEARCH_K = 5
MAX_SEARCH_K = 10

# Response generation
MAX_RESPONSE_TOKENS = 800
FACT_TEMPERATURE = 0.3
CREATIVE_TEMPERATURE = 0.7

# Intent types
INTENT_TYPES = ["fact", "gap", "hypothesis", "contradiction", "general"]

# Intent descriptions for UI
INTENT_DESCRIPTIONS = {
    "fact": "Asking for facts from papers",
    "gap": "Finding research gaps and limitations",
    "hypothesis": "Generating novel hypotheses",
    "contradiction": "Detecting contradictions across papers",
    "general": "General conversation about papers"
}

# Intent colors for UI styling
INTENT_COLORS = {
    "fact": "#4CAF50",
    "gap": "#FF9800",
    "hypothesis": "#9C27B0",
    "contradiction": "#F44336",
    "general": "#2196F3"
>>>>>>> 951aa9ade50f4641f91bcc6c951681eef93dc5b0
}