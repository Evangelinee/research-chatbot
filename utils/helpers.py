"""
Helper utilities for the Research Chatbot.
"""

import hashlib
from typing import List, Dict


def generate_chunk_id(text: str) -> str:
    """
    Generate a unique ID for a text chunk.
    
    Args:
        text: Text content
        
    Returns:
        Short hash ID
    """
    return hashlib.md5(text.encode()).hexdigest()[:8]


def extract_source_files(chunks: List[str], chunk_to_metadata: Dict[str, str]) -> List[str]:
    """
    Extract source file names from retrieved chunks.
    
    Args:
        chunks: List of retrieved text chunks
        chunk_to_metadata: Mapping from chunk text to metadata
        
    Returns:
        List of unique source filenames
    """
    sources = []
    for chunk in chunks:
        if chunk in chunk_to_metadata:
            sources.append(chunk_to_metadata[chunk].get("filename", "Unknown"))
    
    return list(set(sources))


def truncate_text(text: str, max_length: int = 200) -> str:
    """
    Truncate text to a maximum length with ellipsis.
    
    Args:
        text: Input text
        max_length: Maximum length
        
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."


def format_chat_history_for_context(messages: List[Dict], max_messages: int = 5) -> str:
    """
    Format chat history for inclusion in prompts.
    
    Args:
        messages: List of message dictionaries
        max_messages: Maximum number of messages to include
        
    Returns:
        Formatted chat history string
    """
    recent = messages[-max_messages:] if len(messages) > max_messages else messages
    
    formatted = []
    for msg in recent:
        role = "User" if msg["role"] == "user" else "Assistant"
        formatted.append(f"{role}: {msg['content']}")
    
    return "\n".join(formatted)


def validate_api_key(api_key: str) -> bool:
    """
    Basic validation for API key format.
    
    Args:
        api_key: Groq API key
        
    Returns:
        True if format looks valid
    """
    # Groq API keys start with 'gsk_' and are at least 10 chars
    return api_key.startswith("gsk_") and len(api_key) > 10