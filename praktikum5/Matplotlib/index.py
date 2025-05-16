import matplotlib.pyplot as plt

# Membuat List Nama
plt.figtext(0.5, 0.92, "Kelompok 9 - Visualisasi Data", ha='center', fontsize=14, fontweight='bold')
plt.figtext(0.5, 0.80, "- Ilyas Abdul Aziz (0110223292)\n- Muhamad Hilmi Kamil (0110223293)\n- Ferisha Adilla Hidayat (0110223286)",
            ha='center', fontsize=10)

jurusan = ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science']
jumlah_mahasiswa = [120, 150, 100, 80]

plt.bar(jurusan, jumlah_mahasiswa)
plt.title('Jumlah Mahasiswa per Jurusan')
plt.xlabel('Jurusan')
plt.ylabel('Jumlah Mahasiswa')

plt.tight_layout(rect=[0, 0, 1, 0.80])

plt.show()
