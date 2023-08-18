import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

st.title('Static visualization in streamlit with matplotlib and seaborn')

df = pd.read_csv('tips.csv')
st.dataframe(df)