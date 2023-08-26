import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

st.title('Static visualization in streamlit with matplotlib and seaborn')

df = pd.read_csv('tips.csv')
st.dataframe(df)

st.markdown('---')
with st.container():
    st.write('Find the number of Male customers (pie and bar chart)')
    value_counts = df['sex'].value_counts()

    fig, ax =  plt.subplots(figsize=(7, 7))
    ax.pie(value_counts, 
           autopct='%0.2f', 
           labels=value_counts.index)
    
    st.pyplot(fig)

    # draw bar plot 
    fig, ax = plt.subplots() 
    ax.bar(value_counts.index, value_counts) 
    st.pyplot(fig) 

st.markdown('---')

with st.container():
    col1, col2 = st.columns(2) 
    
    with col1:

        st.subheader('Pie chart')
        fig, ax =  plt.subplots()
        ax.pie(value_counts, 
        autopct='%0.2f', 
        labels=value_counts.index)
    
        st.pyplot(fig)

    with col2:
        st.subheader('Bar chart')
        fig, ax = plt.subplots(figsize = (6, 6.2)) 
        ax.bar(value_counts.index, value_counts) 
        st.pyplot(fig) 

    with st.expander('Click here to display count'):
        st.dataframe(value_counts)

      
st.markdown("---")
st.subheader('Interactive charts with input widgets')

data_types = df.dtypes 
cat_cols = tuple(data_types[data_types == 'object'].index)

with st.container():
    feature = st.selectbox('Select the feature yout want to display in the charts:',
                           cat_cols)
    value_counts = df[feature].value_counts()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Pie chart')
        fig, ax = plt.subplots()
        ax.pie(value_counts,
        autopct = '%0.2f',
        labels = value_counts.index) 
        st.pyplot(fig)
    
    with col2:
        st.subheader('Bar chart')
        fig, ax = plt.subplots(figsize = (6, 6.2)) 
        ax.bar(value_counts.index, value_counts) 
        st.pyplot(fig) 

st.markdown('---')
with st.container():
    st.subheader('Find the distribution of values spent by Male and Female customers')
    fig, ax = plt.subplots()
    chart_type = ('boxplot', 'violin', 'kdeplot', 'histogram')
    chart_selection = st.selectbox('Select chart type', chart_type)
    
    if chart_selection == 'boxplot':
        sns.boxplot(x = 'sex', y ='total_bill', data = df)
    
    elif chart_selection == 'violin':
        sns.violinplot(x = 'sex', y = 'total_bill', data = df)

    elif chart_selection == 'kdeplot':
        sns.kdeplot(x = df['total_bill'], hue = df['sex'])

    else:
        sns.histplot(x = 'total_bill', hue = 'sex', data = df)
    
    st.pyplot(fig)

st.markdown('---')
with st.container():
    st.subheader('Find the distribution of average total bill across each day by gender')
    features_to_groupby = ['day', 'sex']
    feature = ['total_bill']
    select_cols = feature + features_to_groupby
    avg_total_bill = df[select_cols].groupby(features_to_groupby).mean().unstack()

    fig, ax =  plt.subplots() 
    avg_total_bill.plot(kind = 'bar', ax = ax)

    plt.xticks(rotation = 0)
    ax.legend(loc = 'center left', bbox_to_anchor = (1, 0.5))

    st.pyplot(fig)

    st.dataframe(avg_total_bill)


st.markdown('---')
with st.container():
    # st.subheader('Find the distribution of average total bill across each day by gender')
    c1, c2, c3 = st.columns(3)

    with c1:
        group_cols = st.multiselect('Select features: ', cat_cols, default=cat_cols[0])
        features_to_groupby = group_cols
        n_features = len(features_to_groupby)
        # st.write(features_to_groupby)

    with c2:
        chart_type = st.selectbox('Select the chart type you want:', 
                                  ('bar', 'area', 'line'))
        
    with c3:
        stack_option = st.radio('Stacked: ', ('Yes', 'No'))
        if stack_option == 'Yes':
            stacked = True
        else:
            stacked = False

    feature = ['total_bill']
    select_cols = feature + features_to_groupby
    if len(features_to_groupby) > 0:
        avg_total_bill = df[select_cols].groupby(features_to_groupby).mean()

        if n_features > 1:
            for i in range(n_features - 1):
                avg_total_bill = avg_total_bill.unstack()

        fig, ax =  plt.subplots() 

    
        avg_total_bill.plot(kind = chart_type, ax = ax, stacked=stacked)

        plt.xticks(rotation = 0)
        ax.legend(loc = 'center left', bbox_to_anchor = (1, 0.5))

        st.pyplot(fig)

    else:
        st.warning('Defina variáveis para agrupar')
        print(len(features_to_groupby))

    with st.expander('Click here to display values'):
        st.dataframe(avg_total_bill)

    st.markdown('---')
    st.subheader('Show the relation between total bill and tip on time')

    fig, ax = plt.subplots() 

    hue_type = st.selectbox('Select the feature to hue', cat_cols)

    sns.scatterplot(x = 'total_bill', y = 'tip', hue = hue_type, data = df, ax = ax)

    st.pyplot(fig)