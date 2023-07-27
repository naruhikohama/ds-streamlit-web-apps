import streamlit as st 
import pandas as pd 
import numpy as np 

# display almost anything
# st.write

st.write("Hello world")

st.write("Welcome to Streamlit App APIs")

st.write(1234)

df = pd.DataFrame({
    'column_1':[1, 2, 3, 4],
    'column_2':[10, 20, 30, 40]
})

st.write(df)

st.write(np.array([1, 2, 3, 4]))