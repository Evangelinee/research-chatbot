# Research Chatbot with Intent Detection

A production-grade Streamlit application that allows you to upload research papers and chat with them using intent-based responses. The chatbot can extract facts, identify research gaps, generate hypotheses, detect contradictions, and have general conversations.

## Features

- Upload up to 5 research papers (PDF format)
- FAISS-powered vector search for efficient retrieval
- 5 intent types with specialized prompt templates:
  - Fact: Extract factual information from papers
  - Gap: Identify research gaps and limitations
  - Hypothesis: Generate novel testable hypotheses
  - Contradiction: Detect conflicting claims across papers
  - General: Natural conversation grounded in papers
- Chat history with source attribution
- Clean modular architecture
- Deployable to Streamlit Cloud for free

