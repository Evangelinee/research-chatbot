<<<<<<< HEAD
"""
Vector Store for Research Chatbot
Handles embedding generation and similarity search
"""

import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
from backend.config import EMBEDDING_MODEL_NAME, EMBEDDING_DIMENSION, SIMILARITY_TOP_K


class VectorStore:
    def __init__(self):
        """Initialize the vector store with embedding model and FAISS index"""
        
        # Load the embedding model
        self.embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)
        
        # Initialize FAISS index
        self.dimension = EMBEDDING_DIMENSION
        self.index = faiss.IndexFlatL2(self.dimension)
        
        # Store chunks and their embeddings
        self.chunks = []
        self.embeddings = []
    
    def create_index(self, chunks):
        """
        Create FAISS index from text chunks
        
        Args:
            chunks: List of text chunks to index
        """
        
        if not chunks:
            return
        
        self.chunks = chunks
        
        # Generate embeddings for all chunks
        embeddings = self.embedding_model.encode(chunks, show_progress_bar=True)
        self.embeddings = embeddings
        
        # Add to FAISS index
        self.index.add(embeddings.astype('float32'))
    
    def search(self, query, k=SIMILARITY_TOP_K):
        """
        Search for similar chunks
        
        Args:
            query: Search query string
            k: Number of results to return
        
        Returns:
            List of similar text chunks
        """
        
        if not self.chunks or self.index.ntotal == 0:
            return []
        
        # Generate embedding for query
        query_embedding = self.embedding_model.encode([query])
        
        # Search in FAISS index
        distances, indices = self.index.search(query_embedding.astype('float32'), k)
        
        # Get the chunks
        results = []
        for idx in indices[0]:
            if idx != -1 and idx < len(self.chunks):
                results.append(self.chunks[idx])
        
        return results
    
    def clear(self):
        """Clear the vector store"""
        
        # Reinitialize FAISS index
        self.index = faiss.IndexFlatL2(self.dimension)
        self.chunks = []
        self.embeddings = []
=======
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
>>>>>>> 951aa9ade50f4641f91bcc6c951681eef93dc5b0
