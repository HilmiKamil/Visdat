import streamlit as st

st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")


st.title("Select Color")
# Color picker
color_code = st.color_picker("Select your Color")
st.header(color_code)