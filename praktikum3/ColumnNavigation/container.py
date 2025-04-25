import streamlit as st
import numpy as np

st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")

st.title("Container")
with st.container():
    st.write("Element Inside Container")
    #Chart Element
    st.line_chart(np.random.randn(40,4))
    st.write("Elemet Outside Container")

st.write("")
st.write("")

#containers 1 (Fungsi container.write())
st.markdown("**Fungsi container.write()**")
container_one = st.container()
container_one.write("Element One Inside Container")
st.write("Element Outside Container")
# Now Inert few more elements in the container_one
container_one.write("Element Two Inside Container")
container_one.line_chart(np.random.randn(40, 4))