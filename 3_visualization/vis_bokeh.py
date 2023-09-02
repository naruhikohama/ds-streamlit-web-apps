import streamlit as st 
import pandas as pd 
from bokeh.plotting import figure 

st.markdown('# Plots with bokeh')

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 8, 4]

p = figure(title='Simple line chart',
           x_axis_label = 'x',
           y_axis_label = 'y')

p.line(x, y, line_width=2)
p.circle(x, y, size = 8)
st.bokeh_chart(p)