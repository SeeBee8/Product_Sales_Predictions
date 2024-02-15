### Sales Prediction App
#Sidebar displaying descriptive stats, summary info, null info buttons
# Dataframe of data, EDA of features, feature vs target plots


import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
pd.set_option("display.max_columns", 100)
from io import StringIO
import functions as fn


st.title("Sales Price Analysis")

## Function to load data
@st.cache_data
def load_data():
    df=pd.read_csv('data/sales_prediction_clean.csv')
    return df

## Image, title and Markdown subheader
#st.image('../Images/__.jpg')
st.markdown('Dataset from [Big Mart Sales Prediction: Analytics Vidhya](https://datahack.analyticsvidhya.com/contest/practice-problem-big-mart-sales-iii/)')



# Load the dataframe
st.header('Product Sales Data')
df = load_data()
st.dataframe(df, width=800)

# Display descriptive statistics
st.sidebar.subheader('Descriptive Statistics')
stats = st.sidebar.button('Statistics')

if stats:
    desc = df.describe().round(2)
    st.dataframe(desc)

# Display summary info
# Create string buffer 
st.sidebar.subheader("Summary Info")
buffer = StringIO()
df.info(buf=buffer)
summary_info = buffer.getvalue()
summary_text = st.sidebar.button('Summary Info')

if summary_text:
    st.text(summary_info)

# Display Null values
st.sidebar.subheader('Null Values')
nulls = df.isna().sum()
null_button = st.sidebar.button("Null Values")

if null_button:
    st.dataframe(nulls)


## Eda Plots subheader
st.sidebar.subheader('Explore Features')

## selectbox for columns
columns = df.columns
features = [col for col in columns if col != 'Feature']
target = 'Feature'

column = st.sidebar.selectbox('Select a Feature', columns, index=None)

## Conditional: if column was chosen
## Check if column is object or numeric and use appropriate plot function
if df[column].dtype == 'object':
    fig = fn.explore_categorical(df, column)
else:
    fig = fn.explore_numeric(df, column)

 ## Show plot
st.markdown('#### Descriptive Plot for {column}')
st.pyplot(fig)


    
## Feature vs Target
st.sidebar.subheader('Compare Features to Item Outlet Sales')
feature = st.sidebar.selectbox('Compare Feature to Item_Outlet_Sales',
                                         features, index=None)

## Check if feature is numeric or object
if df[feature].dtype == 'object':
    fig = fn.plot_categorical_vs_target(df, feature)
else:
    fig = fn.plot_numeric_vs_target(df, feature)

 ## Show plot
st.markdown('#### Comparing {feature} to Item Outlet Sales')
