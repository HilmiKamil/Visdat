import streamlit as st
import time

st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")

# Empty Container
with st.empty():
    for seconds in range(5):
        st.write(f"⌛ {seconds} seconds have passed")
        time.sleep(1)
        st.write("✔ Times up!")