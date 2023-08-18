import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

st.title('Static visualization in streamlit with matplotlib and seaborn')

df = pd.read_csv('tips.csv')
st.dataframe(df)

st.markdown('---')
with st.container():
    st.write('Find the number of Male customers (pie and bar chart)')
    value_counts = df['sex'].value_counts()

    fig, ax =  plt.subplots(figsize=(7, 7))
    ax.pie(value_counts, 
           autopct='%0.2f', 
           labels=value_counts.index)
    
    st.pyplot(fig)

