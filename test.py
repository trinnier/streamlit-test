import streamlit as st
import pandas as pd
import numpy as np

st.title('Test Data')


def load_data(nrows):
    data = pd.read_csv("test_data.csv", nrows=nrows)
    return data

data_load_state = st.text('Loading data...')

data = load_data(10000)

data_load_state.text('Loading data...done!')

st.subheader('Raw data')
st.write(data)
