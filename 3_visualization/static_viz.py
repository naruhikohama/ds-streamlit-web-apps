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

    # draw bar plot 
    fig, ax = plt.subplots() 
    ax.bar(value_counts.index, value_counts) 
    st.pyplot(fig) 

st.markdown('---')

with st.container():
    col1, col2 = st.columns(2) 
    
    with col1:

        st.subheader('Pie chart')
        fig, ax =  plt.subplots()
        ax.pie(value_counts, 
        autopct='%0.2f', 
        labels=value_counts.index)
    
        st.pyplot(fig)

    with col2:
        st.subheader('Bar chart')
        fig, ax = plt.subplots(figsize = (6, 6.2)) 
        ax.bar(value_counts.index, value_counts) 
        st.pyplot(fig) 

    with st.expander('Click here to display count'):
        st.dataframe(value_counts)

      
st.markdown("---")
st.subheader('Interactive charts with input widgets')

data_types = df.dtypes 
cat_cols = tuple(data_types[data_types == 'object'].index)

with st.container():
    feature = st.selectbox('Select the feature yout want to display in the charts:',
                           cat_cols)
    value_counts = df[feature].value_counts()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Pie chart')
        fig, ax = plt.subplots()
        ax.pie(value_counts,
        autopct = '%0.2f',
        labels = value_counts.index) 
        st.pyplot(fig)
    
    with col2:
        st.subheader('Bar chart')
        fig, ax = plt.subplots(figsize = (6, 6.2)) 
        ax.bar(value_counts.index, value_counts) 
        st.pyplot(fig) 