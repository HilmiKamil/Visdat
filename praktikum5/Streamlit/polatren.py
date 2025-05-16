import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Streamlit layout
st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")


data = {
    'Tahun': ['2019', '2020', '2021', '2022', '2023'],
    'Ilmu Komputer': [100, 110, 120, 130, 140],
    'Sistem Informasi': [120, 125, 135, 145, 160],
    'Teknik Informatika': [90,95,100,105,110],
    'Data Science': [70, 75, 80, 85, 90]
}

df = pd.DataFrame(data)

st.title("Visualisasi Tren Jumlah Mahasiswa Memilih Jurusan Komputer (5 Tahun Terakhir)")

filter_tahun = st.multiselect("Pilih Tahun:", df['Tahun'], default=df['Tahun'])

jurusan_list = ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science']
filter_jurusan = st.multiselect("Pilih Jurusan", jurusan_list, default=jurusan_list)

# Filter data berdasarkan input pengguna
filtered_data = df[df['Tahun'].isin(filter_tahun)][['Tahun'] + filter_jurusan]

# Menampilkan data tabel
st.subheader("Data Jumlah Mahasiswa")
st.dataframe(filtered_data)

# Membuat Bar Chart dengan filter
st.subheader("Bar Chart dengan Filter")
fig, ax = plt.subplots(figsize=(10, 6))

# Membuat Bar Chart berdasarkan data yang difilter
x = range(len(filtered_data['Tahun']))
width = 0.2

for i, jur in enumerate(filter_jurusan):
    ax.bar([p + i * width for p in x], filtered_data[jur], width=width, label=jur)

# Menyesuaikan sumbu dan judul
ax.set_title("Jumlah Mahasiswa per Jurusan (Berdasarkan Filter)")
ax.set_xlabel("Tahun")
ax.set_ylabel("Jumlah Mahasiswa")
ax.set_xticks([p + width * len(filter_jurusan) / 2 - width / 2 for p in x])
ax.set_xticklabels(filtered_data['Tahun'])
ax.legend()

# Menampilkan plot di Streamlit
st.pyplot(fig)
