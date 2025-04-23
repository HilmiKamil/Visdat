import streamlit as st

st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")

st.title("Download Button")

#Download Button
down_btn = st.download_button(
    label="Download Image",
    data=open("tupai.jpg", "rb"),
    file_name="tupai.jpg",
    mime="image/jpg"
)

