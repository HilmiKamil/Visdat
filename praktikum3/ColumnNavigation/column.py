import streamlit as st

st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")

#column
col1, col2 = st.columns(2)

col1.write("First Column")
col1.image("landak.jpg")

col2.write("Second Column")
col2.image("penguin.jpg")