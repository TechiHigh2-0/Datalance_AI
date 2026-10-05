import pandas as pd

def generate_statistics(df: pd.DataFrame) -> dict:
    """
    Generates basic descriptive statistics for numerical and categorical columns.
    Returns a dictionary of dataframes for Streamlit display.
    """
    stats = {}
    
    # Numerical statistics
    num_df = df.select_dtypes(include=['number'])
    if not num_df.empty:
        stats['numerical'] = num_df.describe().T.reset_index().rename(columns={'index': 'Column'})
        
    # Categorical statistics
    cat_df = df.select_dtypes(include=['object', 'category', 'bool', 'string'])
    if not cat_df.empty:
        stats['categorical'] = cat_df.describe().T.reset_index().rename(columns={'index': 'Column'})
        
    return stats
