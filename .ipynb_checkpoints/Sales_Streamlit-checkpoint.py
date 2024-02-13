import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
pd.set_option("display.max_columns", 100)
from io import StringIO


st.title("Sales Price Analysis")

## Function to load data
@st.cache_data
def load_data():
    df=pd.read_csv('data/sales_prediction_clean.csv')
    return df

# Load the dataframe
st.header('Product Sales Data')
df = load_data()
st.dataframe(df, width=800)

# Display descriptive statistics
st.markdown("#### Descriptive Statistics")
stats = st.button("Descriptive Statistics")
if stats:
    st.dataframe(df.describe().round(2))

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
null_button = st.button("Null Values')
if nulls:
    st.dataframe(nulls)

