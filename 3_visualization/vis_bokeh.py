import streamlit as st 
import pandas as pd 
from bokeh.plotting import figure 
from bokeh.transform import factor_cmap

st.markdown('# Plots with bokeh')

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 8, 4]

p = figure(title='Simple line chart',
           x_axis_label = 'x',
           y_axis_label = 'y')

p.line(x, y, line_width=2)
p.circle(x, y, size = 8)
st.bokeh_chart(p)

st.markdown('---')
st.markdown('## Plotting with dataframes on bokeh')

data = pd.read_csv('tips.csv')

st.subheader('Scatter plot with total bill and tips')

p = figure(title = 'Scatter plot between total bill and tips')
p.circle(x = 'total_bill', y = 'tip', source = data, size = 5)
st.bokeh_chart(p)

st.markdown('---')
st.subheader('Scatter plot with total bill and tip, coloring by options')

p = figure(title = 'Scatter plot coloring by categories')
select = st.selectbox('Select categories', ('sex', 'smoker', 'day', 'time'))
color_palette = ['blue', 'red', 'green', '#d35400', 'black']

unique_cats = data[select].unique()
index_cmap = factor_cmap(select, color_palette[:len(unique_cats)], sorted(unique_cats))

p.circle('total_bill', 'tip', source = data, fill_color=index_cmap, size=5, legend=select, color=index_cmap)
st.bokeh_chart(p)