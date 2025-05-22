import matplotlib.pyplot as plt

# Membuat List Nama
plt.figtext(0.5, 0.92, "Kelompok 9 - Visualisasi Data", ha='center', fontsize=14, fontweight='bold')
plt.figtext(0.5, 0.80, "- Ilyas Abdul Aziz (0110223292)\n- Muhamad Hilmi Kamil (0110223293)\n- Ferisha Adilla Hidayat (0110223286)",
            ha='center', fontsize=10)

# Contoh data
x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 1, 8, 7, 5]

# Membuat scatter plot
plt.scatter(x, y)

# Menambahkan judul dan label sumbu
plt.title('Contoh Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.tight_layout(rect=[0, 0, 1, 0.80])

# Menampilkan plot
plt.show()
