"""
PDF processing module: Extract text and create chunks.
"""

from pypdf import PdfReader
from io import BytesIO
from typing import List
from backend.config import DEFAULT_CHUNK_SIZE, DEFAULT_CHUNK_OVERLAP


def extract_text_from_pdf(pdf_file) -> str:
    """
    Extract all text content from a PDF file.
    
    Args:
        pdf_file: Uploaded PDF file object
        
    Returns:
        Extracted text as string
    """
    reader = PdfReader(BytesIO(pdf_file.read()))
    text = ""
    
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted
    
    return text


def chunk_text(
    text: str, 
    chunk_size: int = DEFAULT_CHUNK_SIZE, 
    overlap: int = DEFAULT_CHUNK_OVERLAP
) -> List[str]:
    """
    Split text into overlapping chunks for better retrieval.
    
    Args:
        text: Input text to chunk
        chunk_size: Number of words per chunk
        overlap: Number of overlapping words between chunks
        
    Returns:
        List of text chunks
    """
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        # Filter out chunks that are too short
        if len(chunk) > 100:
            chunks.append(chunk)
    
    return chunks


def process_pdf_file(pdf_file) -> tuple:
    """
    Process a single PDF file: extract text and create chunks.
    
    Args:
        pdf_file: Uploaded PDF file object
        
    Returns:
        Tuple of (chunks list, metadata dict)
    """
    text = extract_text_from_pdf(pdf_file)
    chunks = chunk_text(text)
    
    metadata = {
        "filename": pdf_file.name[:50],
        "total_chunks": len(chunks),
        "total_chars": len(text)
    }
    
    return chunks, metadata