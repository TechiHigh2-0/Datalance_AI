import pandas as pd

def load_data(uploaded_file):
    """
    Loads data from a Streamlit UploadedFile object into a pandas DataFrame.
    Supports CSV and XLSX formats.
    """
    if uploaded_file is None:
        return None
        
    filename = uploaded_file.name.lower()
    
    try:
        if filename.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
            return df
        elif filename.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)
            return df
        else:
            raise ValueError("Unsupported file format. Please upload a CSV or XLSX file.")
    except Exception as e:
        raise Exception(f"Error loading file: {str(e)}")
