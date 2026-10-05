import json
import pandas as pd
from src.evidence import execute_plan
from src.ai.gemma_service import get_gemma_response
from src.ai.prompts import SYSTEM_PROMPT, PLANNER_SYSTEM_PROMPT

def answer_question(df: pd.DataFrame, question: str) -> str:
    """
    Orchestrates the 'Ask Your Data' flow.
    1. Parse columns to generate schema info
    2. Gemma interprets query -> JSON plan
    3. Pandas executes plan -> Evidence
    4. Gemma explains evidence -> Final Answer
    """
    if df is None or df.empty:
        return "Dataset is empty. Cannot answer questions."
        
    if not question.strip():
        return "Please ask a valid question."
        
    # Get schema info
    schema_info = {col: str(dtype) for col, dtype in df.dtypes.items()}
    schema_str = "Dataset Schema:\n"
    for col, dtype in schema_info.items():
        sample_vals = df[col].dropna().unique()[:3]
        sample_str = f" (e.g., {', '.join(map(str, sample_vals))})" if len(sample_vals) > 0 else ""
        schema_str += f"- {col} ({dtype}){sample_str}\n"
    
    # 1. Ask Gemma to plan
    plan_prompt = f"{schema_str}\nUser Question: {question}\n\nGenerate the JSON plan:"
    try:
        plan_json_str = get_gemma_response(PLANNER_SYSTEM_PROMPT, plan_prompt)
        
        # Parse JSON
        plan_str_clean = plan_json_str.strip()
        if plan_str_clean.startswith("```json"):
            plan_str_clean = plan_str_clean[7:]
        if plan_str_clean.startswith("```"):
            plan_str_clean = plan_str_clean[3:]
        if plan_str_clean.endswith("```"):
            plan_str_clean = plan_str_clean[:-3]
            
        plan = json.loads(plan_str_clean.strip())
    except Exception as e:
        plan = {"operation": "error", "message": f"Failed to generate a valid analytical plan: {str(e)} (Raw Plan Output: {plan_json_str if 'plan_json_str' in locals() else 'None'})"}
        
    # 2. Python/Pandas calculates deterministic evidence
    evidence = execute_plan(df, plan)
    
    # 3. Gemma explains
    user_prompt = f"User Question: {question}\n\nVerified Analytical Evidence:\n{evidence}"
    try:
        answer = get_gemma_response(SYSTEM_PROMPT, user_prompt)
        return answer
    except Exception as e:
        return f"Failed to get AI answer: {str(e)}"
