"""
PDF Processor for Research Chatbot
Extracts and chunks text from PDF files
"""

import PyPDF2
from backend.config import CHUNK_SIZE, CHUNK_OVERLAP


def extract_text_from_pdf(pdf_file):
    """
    Extract text from PDF file
    
    Args:
        pdf_file: Uploaded PDF file object
    
    Returns:
        Extracted text string
    """
    
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    return text


def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """
    Split text into overlapping chunks
    
    Args:
        text: Input text to chunk
        chunk_size: Size of each chunk in characters
        overlap: Overlap between chunks in characters
    
    Returns:
        List of text chunks
    """
    
    if not text:
        return []
    
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        end = min(start + chunk_size, text_length)
        
        # Try to end at a sentence boundary
        if end < text_length:
            # Look for period, question mark, or exclamation mark
            for i in range(min(end + 100, text_length) - 1, end - 1, -1):
                if text[i] in '.!?':
                    end = i + 1
                    break
        
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        
        # Move start position with overlap
        start = end - overlap
    
    return chunks


def process_pdf_file(pdf_file):
    """
    Process PDF file and return chunks with metadata
    
    Args:
        pdf_file: Uploaded PDF file
    
    Returns:
        Tuple of (chunks list, metadata dict)
    """
    
    # Extract text from PDF
    text = extract_text_from_pdf(pdf_file)
    
    # Chunk the text
    chunks = chunk_text(text)
    
    # Create metadata
    metadata = {
        "filename": pdf_file.name,
        "num_chunks": len(chunks),
        "total_chars": len(text)
    }
    
    return chunks, metadata