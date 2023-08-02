import streamlit as st
import time

st.header('st.progress')
st.caption('Display a progress bar')

# my_bar = st.progress(0)

def progress_bar():
    for pct_complete in range(1, 101):
        time.sleep(0.25)
        pct_complete = min(pct_complete, 100)
        my_bar.progress(pct_complete)

# spinner

with st.spinner("Something is processing..."):
    my_bar = st.progress(0)
    progress_bar()