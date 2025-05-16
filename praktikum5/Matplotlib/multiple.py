import matplotlib.pyplot as plt

# Membuat List Nama
plt.figtext(0.5, 0.92, "Kelompok 9 - Visualisasi Data", ha='center', fontsize=14, fontweight='bold')
plt.figtext(0.5, 0.80, "- Ilyas Abdul Aziz (0110223292)\n- Muhamad Hilmi Kamil (0110223293)\n- Ferisha Adilla Hidayat (0110223286)",
            ha='center', fontsize=10)

jurusan = ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science']
jumlah_mahasiswa = [120, 150, 100, 80]
jumlah_mahasiswa_2024 = [110, 140, 95, 85]

x = range(len(jurusan))
width = 0.4

plt.bar(x, jumlah_mahasiswa, width=width, label='2023', color='skyblue')
plt.bar([p + width for p in x], jumlah_mahasiswa_2024, width=width , label='2024', color='orange')

plt.title('Jumlah Mahasiswa per Jurusan (2023 vs 2024)')
plt.xlabel('Jurusan')
plt.ylabel('Jumlah Mahasiswa')
plt.xticks(rotation=45)
plt.xticks([p + width / 2 for p in x], jurusan)
plt.legend()

plt.tight_layout(rect=[0, 0, 1, 0.80])

plt.show()
