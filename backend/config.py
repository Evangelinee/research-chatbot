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
}