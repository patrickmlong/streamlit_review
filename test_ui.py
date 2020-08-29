import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
#  Welcome to Streamlit Tour!
"""

"""
Here's our first attempt at using data to create a table:
"""
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
     data = pd.read_csv(uploaded_file)
     st.write(data)

if st.checkbox('Show lineplot'):
    st.line_chart(data)

if st.checkbox("barchart"):
    plt.bar(x = "id", y = "home_price", data = data)
    st.pyplot()

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

# st.map(map_data)


st.latex()
