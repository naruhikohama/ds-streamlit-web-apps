import streamlit as st
import pandas as pd 
from pandas_profiling import ProfileReport 
from streamlit_pandas_profiling import st_profile_report 
import sys 
import os 


st.set_page_config(page_title='Data Profiler', layout='wide')

# sidebar 
with st.sidebar:
    uploaded_file = st.file_uploader("Upload data file (csv or xlsx file), not exceeding 10MB") 

    if uploaded_file is not None:
        st.write('Modes of operation')

        minimal = st.checkbox('Minimal report')
        dark_mode = False
        orange_mode = False

        if not minimal:

            display_mode = st.radio('Display mode:', ('Primary', 'Dark', 'Orange'))

            if display_mode == 'Dark':
                dark_mode = True
                orange_mode = False
            
            elif display_mode == 'Orange':
                dark_mode = False
                orange_mode = True
            
            else:
                dark_mode = False
                orange_mode = False
    
    
if uploaded_file is not None:
    # time being, load csv
    df = pd.read_csv(uploaded_file)

    # generate report

    with st.spinner('Generating Report'):
        pr = ProfileReport(df, 
                           minimal = minimal, 
                           dark_mode=dark_mode, 
                           orange_mode=orange_mode
                           )

    st_profile_report(pr)






