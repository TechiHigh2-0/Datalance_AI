import streamlit as st
import pandas as pd
from src.data_loader import load_data
from src.profiler import profile_dataset
from src.statistics import generate_statistics
from src.visualizations import generate_auto_visualizations
from src.ask_data import answer_question
from dotenv import load_dotenv

load_dotenv()

def main():
    st.set_page_config(page_title="DataLens AI", layout="wide")
    st.title("DataLens AI 🔍")
    st.write("Turn raw data into clear decisions. *Pandas calculates. Gemma reasons and communicates.*")
    
    st.sidebar.header("Upload Data")
    uploaded_file = st.sidebar.file_uploader("Upload your dataset (CSV/XLSX)", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        try:
            with st.spinner("Loading dataset..."):
                df = load_data(uploaded_file)
            
            if df is not None:
                st.success("Dataset loaded successfully!")
                
                st.subheader("Dataset Preview")
                st.dataframe(df)
                
                st.subheader("Dataset Profiling")
                with st.spinner("Profiling data..."):
                    profile = profile_dataset(df)
                    
                col1, col2, col3 = st.columns(3)
                col1.metric("Rows", profile.get("num_rows", 0))
                col2.metric("Columns", profile.get("num_cols", 0))
                col3.metric("Duplicate Rows", profile.get("duplicate_rows", 0))
                
                st.write("#### Missing Values & Data Types")
                
                # Combine missing values and dtypes into a summary dataframe
                missing_dict = profile.get("missing_values", {})
                dtypes_dict = profile.get("data_types", {})
                
                summary_df = pd.DataFrame({
                    "Data Type": pd.Series(dtypes_dict),
                    "Missing Values": pd.Series(missing_dict)
                })
                
                st.dataframe(summary_df)
                
                st.subheader("Basic Statistics")
                with st.spinner("Calculating statistics..."):
                    stats = generate_statistics(df)
                    
                if "numerical" in stats:
                    st.write("#### Numerical Properties")
                    st.dataframe(stats["numerical"])
                    
                if "categorical" in stats:
                    st.write("#### Categorical Properties")
                    st.dataframe(stats["categorical"])
                    
                st.subheader("Automatic Visualizations")
                with st.spinner("Generating charts..."):
                    figs = generate_auto_visualizations(df)
                    
                if not figs:
                    st.info("No numerical or categorical columns found to visualize.")
                else:
                    for title, fig in figs:
                        st.plotly_chart(fig, use_container_width=True)
                
                st.subheader("Ask Your Data")
                
                with st.expander("💡 See example questions you can ask"):
                    st.markdown("""
                    **Examples:**
                    • What are the top 5 products by revenue?
                    • Which region contributes the most revenue?
                    • How did revenue change over time?
                    • Compare North and South.
                    • Calculate profit margin.
                    • Find unusual revenue values.
                    • Normalize revenue within each region.
                    • Which customer segment performs best?
                    • Analyze the relationship between quantity and revenue.
                    • Give me a complete analytical report.
                    """)
                    
                question = st.text_input("Ask a question about this dataset:")
                if st.button("Ask Gemma"):
                    with st.spinner("Gemma is reasoning..."):
                        answer = answer_question(df, question)
                        st.info(answer)
                
        except Exception as e:
            st.error(f"Failed to process file: {str(e)}")
    else:
        st.info("👈 Please upload a CSV or XLSX file from the sidebar to begin.")

if __name__ == "__main__":
    main()
