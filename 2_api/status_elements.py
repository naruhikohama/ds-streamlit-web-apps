import streamlit as st
import time

st.header('st.progress')
st.caption('Display a progress bar')

my_bar = st.progress(0)

for pct_complete in range(1, 101):
    time.sleep(0.5)
    my_bar.progress(pct_complete)