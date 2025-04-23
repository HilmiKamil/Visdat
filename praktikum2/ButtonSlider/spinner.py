import streamlit as st
import time

st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")

st.title('Spinner')
#Spinner
with st.spinner('Loading...'):
    time.sleep(5)

st.write('Hello Data Analyst')