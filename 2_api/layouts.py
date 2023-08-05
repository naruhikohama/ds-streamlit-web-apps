import streamlit as st 
import pandas as pd 
import time 

## Load tips.csv 
df = pd.read_csv('tips.csv')

st.dataframe(df)

columns = tuple(df.columns)

side_bar = st.sidebar 

# Do things on sidebar
side_bar.header('Sidebar st.sidebar')
side_bar.caption('Elements that added innsidebar are pinned to left')
side_bar.write('This is sidebar')

## Create widget selctbox 
select_column = side_bar.selectbox(
    "select the you want to display",
    columns
)

side_bar.write(f'You selected the column_name = {select_column}')

# Do thing on main page
st.write('This is page')

st.write(columns)

## Display dataframe 
st.dataframe(df[[select_column]])

