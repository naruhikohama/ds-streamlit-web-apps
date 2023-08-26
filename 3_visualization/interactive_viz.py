import streamlit as st 
import pandas as pd 
import numpy as np 

np.random.seed(101)
sample = pd.DataFrame(np.random.randint(low = 10, high = 20, size = (5, 3)), columns = ['A', 'B', 'C'])

# bar plot 
st.bar_chart(sample)

# area chart
st.area_chart(sample)

# line plot 
st.line_chart(sample)
