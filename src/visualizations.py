import pandas as pd
import plotly.express as px

def generate_auto_visualizations(df: pd.DataFrame):
    """
    Generates a list of plotly figure objects based on the dataset's columns.
    Creates histograms for numerical columns and bar charts for categorical columns (top 10).
    """
    figs = []
    
    # Numerical columns: Histograms (max 5 to avoid clutter)
    num_cols = df.select_dtypes(include=['number']).columns.tolist()
    for col in num_cols[:5]:
        # Skip id columns or very low variance columns if needed, but keep it simple for now
        fig = px.histogram(df, x=col, title=f"Distribution of {col}")
        figs.append((f"Histogram: {col}", fig))
        
    # Categorical columns: Bar charts for value counts (max 5)
    cat_cols = df.select_dtypes(include=['object', 'category', 'bool', 'string']).columns.tolist()
    for col in cat_cols[:5]:
        # Get top 10 categories
        val_counts = df[col].value_counts().reset_index().head(10)
        val_counts.columns = [col, 'Count']
        fig = px.bar(val_counts, x=col, y='Count', title=f"Top Categories in {col}")
        figs.append((f"Bar Chart: {col}", fig))
        
    return figs
