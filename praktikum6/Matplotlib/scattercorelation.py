import matplotlib.pyplot as plt

# Membuat List Nama
plt.figtext(0.5, 0.92, "Kelompok 9 - Visualisasi Data", ha='center', fontsize=14, fontweight='bold')
plt.figtext(0.5, 0.80, "- Ilyas Abdul Aziz (0110223292)\n- Muhamad Hilmi Kamil (0110223293)\n- Ferisha Adilla Hidayat (0110223286)",
            ha='center', fontsize=10)

# Data dummy
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]

# Data tambahan
kelembapan = [60, 65, 70, 75, 80, 85, 90, 95, 100]
ukuran_titik = [200, 220, 240, 260, 280, 300, 320, 340, 360]

# Scatter Plot dengan ukuran dan warna yang bervariasi
plt.scatter(suhu, penjualan, c=kelembapan, s=ukuran_titik, cmap='coolwarm', alpha=0.6)
plt.title('Hubungan Penjualan, Suhu, dan Kelembapan')
plt.xlabel('Suhu (°C)')
plt.ylabel('Penjualan Es Krim')
plt.colorbar(label='Kelembapan (%)')

plt.tight_layout(rect=[0, 0, 1, 0.80])

plt.show()
