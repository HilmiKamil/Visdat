import streamlit as st
import pandas as pd
import numpy as np

st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")

df = pd.DataFrame(
    np.random.rand(30, 10),
    columns=('col_no %d' % i for i in range(10))
)

#st.dataframe(df)
st.dataframe(df.style.highlight_min(axis=0))