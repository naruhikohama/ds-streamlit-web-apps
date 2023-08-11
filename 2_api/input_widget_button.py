import streamlit as st 
import pandas as pd 
import numpy as np 
import os

# load data 
data = pd.read_csv('tips.csv')

def display_data_random(df):
    sample = df.sample(5)
    return sample

# button widget 
st.subheader('Dispalying random 5 rows with button')
st.caption('Click on the button below to display the row randomly')
button = st.button('Display random 5 rows')
if button:
    sample = display_data_random(data)
    st.dataframe(sample)
