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

# Layout with columns 

st.header('Columns: st.columns')

col1, col2, col3 = st.columns(3)

with col1: 
    st.subheader('column-1')
    st.image('./media/image.jpg')

with col2: 
    st.subheader('column-2')
    st.dataframe(df)

with col3: 
    st.subheader('column-3')
    st.dataframe(df[[select_column]])


# Expander

st.header('Expander: st.expander')

with st.expander('Some explanation'):
    st.write(
        """
        Insert a multi-element container that can be expanded/collapsed.
        Inserts a container into your app that can be used to hold multiple elements and can be expanded or collapsed.
        When collpased, all that is visible is the provided label.
        """
    )

    st.code(
        """
        # You create expander with st.write

        import streamlit as st 
        st.expander('your label for the expander here')
        st.write('text that will be hidden when collapsed goes here')
        """, 
        language='python'
    )