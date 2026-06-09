"""
Intent Handler for Research Chatbot
Handles different response types using Groq API
"""

import groq
from backend.config import INTENT_PROMPTS

class IntentHandler:
    def __init__(self, api_key, model="mixtral-8x7b-32768"):
        """
        Initialize the intent handler with Groq API
        
        Args:
            api_key: Groq API key
            model: Model to use (default: mixtral-8x7b-32768)
                   Alternatives: llama3-70b-8192, gemma2-9b-it
        """
        self.client = groq.Groq(api_key=api_key)
        self.model = model
        self.api_key = api_key
    
    def generate_response(self, question, context_chunks, intent, chat_history=None):
        """
        Generate a response based on the intent and context
        
        Args:
            question: User's question
            context_chunks: List of relevant text chunks from papers
            intent: Type of response (fact, gap, hypothesis, contradiction, general)
            chat_history: Previous conversation history
        
        Returns:
            Generated response string
        """
        
        # Combine context chunks
        context = "\n\n".join(context_chunks)
        
        # Get system prompt based on intent
        system_prompt = INTENT_PROMPTS.get(intent, INTENT_PROMPTS["general"])
        
        # Prepare conversation history
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "system", "content": f"Context from research papers:\n{context}"}
        ]
        
        # Add chat history if provided (last 3 exchanges)
        if chat_history:
            for msg in chat_history[-6:]:  # Last 3 exchanges
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })
        
        # Add current question
        messages.append({"role": "user", "content": question})
        
        try:
            # Generate response using Groq
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=1000,
                top_p=1,
                stream=False
            )
            
            return completion.choices[0].message.content
            
        except Exception as e:
            # Try fallback model if current one fails
            if "model_decommissioned" in str(e) or "not supported" in str(e):
                fallback_models = ["llama3-70b-8192", "gemma2-9b-it", "mixtral-8x7b-32768"]
                for fallback in fallback_models:
                    if fallback != self.model:
                        try:
                            self.model = fallback
                            completion = self.client.chat.completions.create(
                                model=self.model,
                                messages=messages,
                                temperature=0.7,
                                max_tokens=1000,
                                top_p=1,
                                stream=False
                            )
                            return completion.choices[0].message.content
                        except:
                            continue
            raise e