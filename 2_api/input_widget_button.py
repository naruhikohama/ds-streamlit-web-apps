import streamlit as st 
import pandas as pd 
import numpy as np 
from datetime import date
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
st.subheader('Radio button: st.radio')

radio_button = st.radio('What is your favorite color?', 
                        ('White', 'Blue', 'Green', 'Red'))

st.write('Your favorite color is ', radio_button)

# select box
st.markdown('---')
st.subheader('Select box: st.selectbox')

select_box = st.selectbox('What do you want to learn most?',
                           ('Basics of python', 'Data science', 'Machine learning', 'Statistics', 'Data vizualisation'))

st.write('Your top priority for now is: ', select_box)

# multi select box
st.markdown('---')
st.subheader('Multi-selection box: st.multiselect')

options = st.multiselect('What programming languages do you know?',
               ['Python', 'R', 'Julia', 'Javascript', 'Java', 'Rust', 'Others'])

st.write('You selected: ', options)

# slider
st.markdown('---')
st.subheader('Slider: st.slider')

slider = st.slider("How much percentage is your phone battery right now?", 0, 100, 1)

st.markdown(f"Your battery needs a cahrge of *{100-slider}%* to get to 100%")

# text input
st.markdown('---')
st.subheader('Text as inpu: st.text_input or st.number_input')

with st.container():

    name = st.text_input('Your name: ')
    age = st.number_input('What is your age: ', min_value = 0, max_value = 150, value = 21, step = 1)
    description = st.text_area('Comments', height=150)
    dob = st.date_input('Select your date of birth', min_value = date(1900, 1, 1))

    submit_button = st.button('Submit again')

    if submit_button:
        info = {
            'Name': name,
            'Date of birth': dob,
            'Age': age,
            'Comments': description          
            }
    
        st.json(info)

# File uploader
st.markdown('---')
st.subheader('File uploader: st.file_uploader')

uploaded_file = st.file_uploader('Choose a file')
save_button = st.button('Save file')
if save_button:
    if uploaded_file is not None:
        with open(os.path.join('./save_folder', uploaded_file.name), mode = 'wb') as f:
            f.write(uploaded_file.getbuffer())

        st.success('File uploaded successfully!')

    else:
        st.warning('Please select the file you want to upload.')