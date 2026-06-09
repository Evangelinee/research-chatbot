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