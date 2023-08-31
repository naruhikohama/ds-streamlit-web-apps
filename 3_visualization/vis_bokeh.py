import streamlit as st 
import pandas as pd 
from bokeh.plotting import figure 

st.markdown('# Plots with bokeh')

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 8, 4]

p = figure(title='Simple line chart')

p.line(x, y)
st.bokeh_chart(p)