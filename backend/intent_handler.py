<<<<<<< HEAD
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
=======
"""
Intent handler module: Manages intent-specific prompts and response generation.
"""

from groq import Groq
from typing import List, Dict
from backend.config import (
    LLM_MODEL_NAME, 
    MAX_RESPONSE_TOKENS,
    FACT_TEMPERATURE,
    CREATIVE_TEMPERATURE
)


class IntentHandler:
    """Handles intent detection and response generation."""
    
    def __init__(self, api_key: str):
        """
        Initialize the Groq client.
        
        Args:
            api_key: Groq API key
        """
        self.client = Groq(api_key=api_key)
    
    def get_intent_prompt(self, intent: str, question: str, context: str, chat_history: str) -> str:
        """
        Generate intent-specific prompt template.
        
        Args:
            intent: Selected intent type
            question: User's question
            context: Retrieved paper excerpts
            chat_history: Previous conversation history
            
        Returns:
            Formatted prompt for the LLM
        """
        
        base_context = f"""
Chat History (last 5 exchanges):
{chat_history}

User Question: {question}

Relevant Paper Excerpts:
{context}
"""
        
        prompts = {
            "fact": f"""You are a research assistant answering FACTS from papers.

{base_context}

INSTRUCTIONS:
1. Answer ONLY using the excerpts above
2. Be factual and precise
3. Cite sources: "According to [paper name]..."
4. If answer not found, say "I cannot find this in the uploaded papers"
5. Do not add information from outside the excerpts""",

            "gap": f"""You are a research gap analyzer. Find what is MISSING.

{base_context}

INSTRUCTIONS:
1. Identify 2-3 specific research gaps or limitations
2. Format as bullet points
3. For each gap, explain WHY it matters
4. Suggest HOW to investigate this gap
5. Be critical: what did papers NOT address?""",

            "hypothesis": f"""You are a hypothesis generator for future research.

{base_context}

INSTRUCTIONS:
1. Generate 2-3 novel, testable hypotheses
2. Format each: "Hypothesis X: [statement] because [reasoning]"
3. Suggest experimental approaches to test each
4. Be creative but grounded in the excerpts
5. Think about what the papers imply but did not test""",

            "contradiction": f"""You are a contradiction detector across multiple papers.

{base_context}

INSTRUCTIONS:
1. Find conflicting claims, results, or methodologies
2. For each contradiction: "Paper A says X, but Paper B says Y"
3. If no contradictions found, state "Papers appear consistent on this topic"
4. Suggest possible reasons for disagreements
5. Note which papers support which position""",

            "general": f"""You are a helpful research assistant.

{base_context}

INSTRUCTIONS:
1. Answer naturally and conversationally
2. Stay grounded in the excerpts
3. Be helpful even if the question is broad
4. If unsure, say so and suggest what information would help"""
        }
        
        return prompts.get(intent, prompts["general"])
    
    def generate_response(
        self, 
        question: str, 
        context_chunks: List[str], 
        intent: str, 
        chat_history: List[Dict]
    ) -> str:
        """
        Generate a response using the selected intent.
        
        Args:
            question: User's question
            context_chunks: Retrieved relevant text chunks
            intent: Selected intent type
            chat_history: Previous conversation messages
            
        Returns:
            Generated response text
        """
        
        if not context_chunks:
            return "I could not find relevant information in the uploaded papers. Please try rephrasing your question."
        
        # Combine context chunks
        context = "\n\n---\n\n".join(context_chunks)
        
        # Format chat history
        history_text = "\n".join([
            f"{msg['role']}: {msg['content']}" 
            for msg in chat_history[-5:]
        ])
        
        # Get intent-specific prompt
        prompt = self.get_intent_prompt(intent, question, context, history_text)
        
        # Set temperature based on intent
        temperature = CREATIVE_TEMPERATURE if intent in ["hypothesis", "gap"] else FACT_TEMPERATURE
        
        try:
            response = self.client.chat.completions.create(
                model=LLM_MODEL_NAME,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=MAX_RESPONSE_TOKENS
            )
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error generating response: {str(e)}. Please try again."
>>>>>>> 951aa9ade50f4641f91bcc6c951681eef93dc5b0
