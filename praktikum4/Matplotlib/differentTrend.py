import matplotlib.pyplot as plt

# Membuat List Nama
plt.figtext(0.5, 0.92, "Kelompok 9 - Visualisasi Data", ha='center', fontsize=14, fontweight='bold')
plt.figtext(0.5, 0.80, "- Ilyas Abdul Aziz (0110223292)\n- Muhamad Hilmi Kamil (0110223293)\n- Ferisha Adilla Hidayat (0110223286)",
            ha='center', fontsize=10)

# Data sample
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10, 20, 15, 25, 30, 45, 40, 50, 60, 55, 65, 70]
product_B_sales = [5, 10, 8, 15, 18, 20, 22, 30, 25, 35, 40, 45]

# Line Plot
plt.plot(months, product_A_sales, label='Product A Trend', linestyle='--', color='blue')
plt.plot(months, product_B_sales, label='Product B Trend', linestyle='-.', color='red')
plt.title('Tren Penjualan Produk Per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penjualan')
plt.legend()

plt.tight_layout(rect=[0, 0, 1, 0.80])

plt.grid(True)
plt.show()
