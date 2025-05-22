import streamlit as st
import matplotlib.pyplot as plt

suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]

#Data Kategori Hari
penjualan_kerja = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_akhir_pekan = [60, 70, 80, 100, 110, 120, 140, 160, 200]

st.title('Visualisasi Hubungan Penjualan Es Krim dengan Suhu')

fig, ax = plt.subplots()
ax.scatter(suhu, penjualan, color='blue')
ax.set_title('Hubungan Penjualan Es Krim dan Suhu')
ax.set_xlabel('Suhu(°C)')
ax.set_ylabel('Penjualan Es Krim')

st.pyplot(fig)

#Kustomisasi Scatter Plot

fig, ax = plt.subplots()
ax.scatter(suhu, penjualan, color='orange', s=100, edgecolor='black')
ax.set_title('Hubungan Penjualan Es Krim dan Suhu (Kustom)')
ax.set_xlabel('Suhu(°C)')
ax.set_ylabel('Penjualan Es Krim')
ax.grid(True)

st.pyplot(fig)

#Multiple Scatter Plot

fig, ax = plt.subplots()
ax.scatter(suhu, penjualan_kerja, color='green', label='Hari Kerja', s=80)
ax.scatter(suhu, penjualan_akhir_pekan, color='purple', label='Akhir Pekan' , s=80)
ax.set_title('Hubungan Penjualan Es Krim Berdasarkan Hari')
ax.set_xlabel('Suhu(°C)')
ax.set_ylabel('Penjualan Es Krim')
ax.legend()

st.pyplot(fig)