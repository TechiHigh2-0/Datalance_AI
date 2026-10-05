import pandas as pd

def generate_evidence(df: pd.DataFrame, question: str) -> str:
    """
    Determines relevant analytical operation and returns verified evidence string.
    Since we don't have a complex NLP router yet, we will provide a comprehensive summary
    of the dataframe tailored to basic questions, plus allow simple keyword routing.
    """
    evidence = []
    evidence.append(f"Dataset has {len(df)} rows and {len(df.columns)} columns.")
    evidence.append(f"Columns: {', '.join(df.columns)}")
    
    # Very naive routing for MVP
    q_lower = question.lower()
    
    if "average" in q_lower or "mean" in q_lower:
        num_cols = df.select_dtypes(include=['number']).columns
        means = df[num_cols].mean().to_dict()
        evidence.append(f"Averages for numerical columns: {means}")
        
    if "max" in q_lower or "highest" in q_lower or "top" in q_lower:
        num_cols = df.select_dtypes(include=['number']).columns
        maxes = df[num_cols].max().to_dict()
        evidence.append(f"Maximum values for numerical columns: {maxes}")
        
    if "min" in q_lower or "lowest" in q_lower or "bottom" in q_lower:
        num_cols = df.select_dtypes(include=['number']).columns
        mins = df[num_cols].min().to_dict()
        evidence.append(f"Minimum values for numerical columns: {mins}")
        
    # Always include basic stats just in case
    num_cols = df.select_dtypes(include=['number']).columns
    if len(num_cols) > 0:
        sums = df[num_cols].sum().to_dict()
        evidence.append(f"Sums for numerical columns: {sums}")
        
    return "\n".join(evidence)
