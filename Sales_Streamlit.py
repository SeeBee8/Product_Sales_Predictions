### Sales Prediction App
#Sidebar displaying descriptive stats, summary info, null info buttons
# Dataframe of data, EDA of features, feature vs target plots


import pandas as pd
import streamlit as st
import matplotlib
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
st.markdown('#### Descriptive Statistics')
stats = st.button('Show Statistics')

if stats:
    desc = df.describe().round(2)
    st.dataframe(desc)

# Display summary info
# Create string buffer 
st.markdown("#### Summary Info")
buffer = StringIO()
df.info(buf=buffer)
summary_info = buffer.getvalue()
summary_text = st.button('Show Summary Info')

if summary_text:
    st.text(summary_info)

# Display Null values
st.markdown('#### Null Values')
nulls = df.isna().sum()
null_button = st.button("Show Null Values")

if null_button:
    st.dataframe(nulls)


#### EDA
st.markdown("#### Display Plot for Features")
# Add a selectbox for all possible features
column = st.selectbox(label="Select a feature", options=df.columns)

# Conditional statement to determine which function to use
if df[column].dtype == 'object':
    plt, ax  = fn.explore_categorical(df, column)
else:
    fig = fn.explore_numeric(df, column)
    

st.pyplot(fig)

###COMPARE FEATURES TO TARGET
options=(df.columns).drop("Item_Outlet_Sales")
st.markdown("#### Compare Features to Item_Outlet_Sales")
# Add a selectbox for all possible features
column = st.selectbox(label="Select a feature", options=options)

# Conditional statement to determine which function to use
if df[column].dtype == 'object':
    plt, ax  = fn.plot_categorical_vs_target(df, x=column)
else:
    plt, ax = fn.plot_numeric_vs_target(df, x=column)
    

st.pyplot(plt)

