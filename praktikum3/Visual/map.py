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

st.title('Map')
# Latitude and Longitude
locate_map = pd.DataFrame(
    np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078], 
    columns=['latitude', 'longitude']
)
# Map Function
st.map(locate_map)