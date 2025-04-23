import streamlit as st

st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")


st.title("Text Box")

#textbox 
# Creating Text box with 10 as character limit
name = st.text_input("Enter your Name", max_chars=10)
password = st.text_input("Enter your password", type='password')

st.write("Your Name is ", name)
st.write("Your Password is ", password)

