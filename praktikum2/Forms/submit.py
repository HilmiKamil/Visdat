import streamlit as st

st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")


my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')

#Submit button
submit_button = my_form.form_submit_button(label='Submit')

st.write(a)