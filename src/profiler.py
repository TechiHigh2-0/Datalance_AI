import pandas as pd

def profile_dataset(df: pd.DataFrame) -> dict:
    """
    Deterministically profiles a pandas DataFrame.
    Returns a dictionary of useful metadata and basic statistics.
    """
    if df is None or df.empty:
        return {"error": "DataFrame is empty or None."}
        
    profiling_results = {
        "num_rows": len(df),
        "num_cols": len(df.columns),
        "columns": list(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "data_types": df.dtypes.astype(str).to_dict(),
    }
    
    return profiling_results
