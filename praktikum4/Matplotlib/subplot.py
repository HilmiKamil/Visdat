import matplotlib.pyplot as plt

# Data sample
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10, 20, 15, 25, 30, 45, 40, 50, 60, 55, 65, 70]
product_B_sales = [5, 10, 8, 15, 18, 20, 22, 30, 25, 35, 40, 45]

fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# Membuat List Nama
plt.figtext(0.5, 0.92, "Kelompok 9 - Visualisasi Data", ha='center', fontsize=14, fontweight='bold')
plt.figtext(0.5, 0.80, "- Ilyas Abdul Aziz (0110223292)\n- Muhamad Hilmi Kamil (0110223293)\n- Ferisha Adilla Hidayat (0110223286)",
            ha='center', fontsize=10)

# Product A
axs[0].plot(months, product_A_sales, label='Product A', color='blue', marker='o')
axs[0].set_title('Penjualan Produk A Per Bulan')
axs[0].set_xlabel('Bulan')
axs[0].set_ylabel('Jumlah Penjualan')
axs[0].legend()
axs[0].grid(True)

# Product B
axs[1].plot(months, product_B_sales, label='Product B', color='red', marker='x')
axs[1].set_title('Penjualan Produk B Per Bulan')
axs[1].set_xlabel('Bulan')
axs[1].set_ylabel('Jumlah Penjualan')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.78])
plt.show()
