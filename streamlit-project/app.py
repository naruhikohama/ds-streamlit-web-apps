import streamlit as st
import pandas as pd 
from pandas_profiling import ProfileReport 
from streamlit_pandas_profiling import st_profile_report 
import sys 
import os 

# sidebar 
with st.sidebar:
    uploaded_file = st.file_uploader("Upload data file (csv or xlsx file), not exceeding 10MB") 
    
if uploaded_file is not None:
    # time being, load csv
    df = pd.read_csv(uploaded_file)

    st.dataframe(df.head(10))






