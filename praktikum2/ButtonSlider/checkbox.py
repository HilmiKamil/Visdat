import streamlit as st

st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")

st.title('Checkboxes')
st.write('Select your Hobbies:')
#Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Traveling')