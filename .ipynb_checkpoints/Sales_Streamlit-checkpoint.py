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


st.title("Sales Price Analysis")

## Function to load data
@st.cache_data
def load_data():
    df=pd.read_csv('data/sales_prediction_clean.csv')
    return df

## Image, title and Markdown subheader
#st.image('../Images/__.jpg')
st.title('Sales Prediction App')
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


# Create string buffer 
buffer = StringIO()
#Write info into the buffer
df.info(buf=buffer)
summary_info = buffer.getvalue()
st.markdown('#### Summary Info')
summary_text = st.button('Summary Info')
if summary_text:
    st.text(summary_info)

# Display Null values
st.markdown('#### Null Values')
nulls = df.isna().sum()
null_button = st.button("Null Values")
if null_button:
    st.dataframe(nulls)

