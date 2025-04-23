import streamlit as st

st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")

st.write("Displaying an Images")
# Displaying Image by specifying path
st.image("img/dog.jpg")
# Image Courtesy by unsplash
st.write("Image Courtesy: pinterest.com")

import streamlit as st
# Image Courtesy
st.write("Displaying Multiple Images")
# Listing out animal images
animal_images = [
    'img/penguin.jpg',
    'img/kelinci.jpg',
    'img/landak.jpg',
    'img/tupai.jpg',
]
# Displaying Multiple images with width 150
st.image(animal_images, width=150)
# Image Courtesy
st.write("Image Courtesy: Pinterest")