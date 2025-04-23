import streamlit as st

st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")

st.title('Multi-Select')

#Multi_Select
hobbies = st.multiselect(
    'What are your Hobbies',
    ['Reading', 'Traveling', 'Watching Movies/TV Series', 'Playing', 'Drawing'],
    ['Reading', 'Watching Movies/TV Series']
)