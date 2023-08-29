import streamlit as st 
import pandas as pd 
import numpy as np 

import plotly.express as px 

data = pd.read_csv('tips.csv')  

# 1. Draw histogram for total bill 
st.subheader('Draw histogram for total bill')
fig = px.histogram(data, x = 'total_bill')

st.plotly_chart(fig)

# 2. Draw histogram for total bill by sex
st.markdown('---')
st.subheader('Draw histogram for total bill by sex')
fig = px.histogram(data, x = 'total_bill', color = 'sex')

st.plotly_chart(fig)

st.markdown('---')
st.subheader('Draw a hsitogram for total bill and color by (\'sex, smoker, day, time\')')

select = st.selectbox('Select the category to color', 
                      ('sex', 'smoker', 'day', 'time'))

fig = px.histogram(data_frame=data, x = 'total_bill', color = select)
st.plotly_chart(fig)