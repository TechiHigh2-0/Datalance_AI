import pandas as pd
from src.evidence import generate_evidence
from src.ai.gemma_service import get_gemma_response
from src.ai.prompts import SYSTEM_PROMPT

def answer_question(df: pd.DataFrame, question: str) -> str:
    """
    Orchestrates the 'Ask Your Data' flow.
    1. Generate evidence using Pandas
    2. Format prompt
    3. Call Gemma
    """
    if df is None or df.empty:
        return "Dataset is empty. Cannot answer questions."
        
    if not question.strip():
        return "Please ask a valid question."
        
    # 1. Python/Pandas calculates deterministic evidence
    evidence = generate_evidence(df, question)
    
    # 2. Format the user prompt
    user_prompt = f"User Question: {question}\n\nVerified Analytical Evidence:\n{evidence}"
    
    # 3. Gemma reasons and communicates
    try:
        answer = get_gemma_response(SYSTEM_PROMPT, user_prompt)
        return answer
    except Exception as e:
        return f"Failed to get AI answer: {str(e)}"
