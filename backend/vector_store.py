"""
Vector store module: Create embeddings and search using FAISS.
"""

import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
from typing import List, Tuple
from backend.config import EMBEDDING_MODEL_NAME, DEFAULT_SEARCH_K


class VectorStore:
    """Manages embeddings and similarity search for document chunks."""
    
    def __init__(self):
        """Initialize the embedding model."""
        self.model = SentenceTransformer(EMBEDDING_MODEL_NAME)
        self.index = None
        self.chunks = []
        self.embeddings = None
    
    def create_index(self, chunks: List[str]) -> None:
        """
        Create FAISS index from text chunks.
        
        Args:
            chunks: List of text chunks to index
        """
        self.chunks = chunks
        
        if not chunks:
            return
        
        # Generate embeddings
        self.embeddings = self.model.encode(chunks)
        
        # Create FAISS index
        dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(np.array(self.embeddings).astype('float32'))
    
    def search(self, query: str, k: int = DEFAULT_SEARCH_K) -> List[str]:
        """
        Search for relevant chunks given a query.
        
        Args:
            query: User's question
            k: Number of chunks to retrieve
            
        Returns:
            List of relevant text chunks
        """
        if not self.index or not self.chunks:
            return []
        
        # Generate query embedding
        query_embedding = self.model.encode([query])
        
        # Search FAISS index
        k = min(k, len(self.chunks))
        distances, indices = self.index.search(
            np.array(query_embedding).astype('float32'), 
            k
        )
        
        # Return retrieved chunks
        return [self.chunks[i] for i in indices[0] if i < len(self.chunks)]
    
    def clear(self) -> None:
        """Clear all stored data."""
        self.index = None
        self.chunks = []
        self.embeddings = None
    
    def get_stats(self) -> dict:
        """Get statistics about the current vector store."""
        return {
            "total_chunks": len(self.chunks),
            "has_index": self.index is not None,
            "embedding_dimension": self.embeddings.shape[1] if self.embeddings is not None else 0
        }