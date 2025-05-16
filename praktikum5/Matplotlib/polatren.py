import matplotlib.pyplot as plt

# Membuat List Nama
plt.figtext(0.5, 0.92, "Kelompok 9 - Visualisasi Data", ha='center', fontsize=14, fontweight='bold')
plt.figtext(0.5, 0.80, "- Ilyas Abdul Aziz (0110223292)\n- Muhamad Hilmi Kamil (0110223293)\n- Ferisha Adilla Hidayat (0110223286)",
            ha='center', fontsize=10)

jurusan = ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science']
tahun = ['2019', '2020', '2021', '2022', '2023']
data = {
    'Ilmu Komputer': [100, 110, 120, 130, 140],
    'Sistem Informasi': [120, 125, 135, 145, 160],
    'Teknik Informatika': [90, 95, 100, 105, 110],
    'Data Science': [70, 75, 80, 85, 90]
}

width = 0.2
x = range(len(tahun))

plt.bar(x, data['Ilmu Komputer'], width=width, label='Ilmu Komputer', color='blue')
plt.bar([p + width for p in x], data['Sistem Informasi'], width=width , label='Sistem Informasi', color='orange')
plt.bar([p + width * 2 for p in x], data['Teknik Informatika'], width=width , label='Teknik Informatika', color='green')
plt.bar([p + width * 3 for p in x], data['Data Science'], width=width , label='Data Science', color='red')

plt.title('Tren Jumlah Mahasiswa per Jurusan (2019-2023)')
plt.xlabel('Jurusan')
plt.ylabel('Jumlah Mahasiswa')
plt.xticks([p + width * 1.5 for p in x], tahun)
plt.legend()

plt.tight_layout(rect=[0, 0, 1, 0.80])

plt.show()
