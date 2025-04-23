# importing Necessary Libraries
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10))
)

# defining multiple arguments in write function
st.write('Here is our Data:', df, 'Data is in dataframe format.\n', "\nWrite is Super function")

# Defining random Values for Chart
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b']
)

# Defining Chart
chart = alt.Chart(df).mark_bar().encode(
    x='a',
    y='b',
    tooltip=['a', 'b']
)

# Defining Chart in write() function
st.write(chart)