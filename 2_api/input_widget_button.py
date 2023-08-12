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


# checkbox
st.markdown('---')
st.subheader('Checkbox: st.checkbox')

agree = st.checkbox('I agree to terms and conditions')
st.write('checkbox status: ', agree)

# mulitple checkboxes
st.subheader('Multiple checkboxes')
with st.container():
    st.info('What technologies you are involved with right now:')

    python = st.checkbox('Python')
    data_science = st.checkbox('Data Science')
    ai_ml = st.checkbox('AI - ML')
    r = st.checkbox('R')
    julia = st.checkbox('Julia')
    javascript = st.checkbox('Javascript')

    tech_button = st.button('Submit')

    if tech_button:
        tech_dict = {
            'Python': python,
            'Data Science': data_science,
            'AI - ML': ai_ml,
            'R': r,
            'Julia': julia,
            'Javascript': javascript
        }

        st.json(tech_dict)

# radio button
st.markdown('---')
st.subheader('RAadio button: st.radio')

radio_button = st.radio('What is your favorite color?', 
                        ('White', 'Blue', 'Green', 'Red'))

st.write('Your favorite color is ', radio_button)