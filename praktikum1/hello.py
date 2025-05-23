import streamlit as st
from vega_datasets import data


st.title("Bar Chart")

source = data.barley()

st.bar_chart(source, x="year", y="yield", color="site", stack=False)