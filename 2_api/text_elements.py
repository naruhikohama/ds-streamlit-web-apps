import streamlit as st 

# title
st.title("Using st.title(), yout can display the text in the title format")

# header
st.header("This is a header")
st.caption("The text inside st.header() is in header formatting")

# subheader
st.subheader("This is a subheader")
st.caption("The text inside st.subheader() is in subheader formatting")

# display the code in page
body = """
import numpy as np

def generate_random(size):
    rand = np.random.random(size = size)
    return rand

number = generate_random(10)
"""

st.code(body, language = 'python')

# Latex
st.subheader("Latex")

formula = """
a + ar + ar^2 + ar^3 + \cdots + ar^(n-1) = \sum_{k=0}^{n-1}ar^k
"""

st.latex(formula)