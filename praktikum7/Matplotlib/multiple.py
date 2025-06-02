import matplotlib.pyplot as plt
import numpy as np

# Membuat List Nama
plt.figtext(0.5, 0.92, "Kelompok 9 - Visualisasi Data", ha='center', fontsize=14, fontweight='bold')
plt.figtext(0.5, 0.80, "- Ilyas Abdul Aziz (0110223292)\n- Muhamad Hilmi Kamil (0110223293)\n- Ferisha Adilla Hidayat (0110223286)",
            ha='center', fontsize=10)

# Data tambahan untuk periode berbeda
stores = ['Store A', 'Store B', 'Store C']
q1_male = [150, 180, 160]
q1_female = [140, 200, 180]
q2_male = [170, 190, 175]
q2_female = [130, 210, 160]
q3_male = [160, 185, 170]
q3_female = [135, 195, 165]
q4_male = [155, 175, 168]
q4_female = [125, 205, 158]

x = np.arange(len(stores))

# Lebar batang
bar_width = 0.2

# Multiple Stacked Bar Chart
plt.bar(x - bar_width * 1.5, q1_male, label='Q1 Male', color='lightblue', width=bar_width)
plt.bar(x - bar_width * 1.5, q1_female, bottom=q1_male, label='Q1 Female', color='pink', width=bar_width)

plt.bar(x - bar_width / 2, q2_male, label='Q2 Male', color='blue', width=bar_width)
plt.bar(x - bar_width / 2, q2_female, bottom=q2_male, label='Q2 Female', color='red', width=bar_width)

plt.bar(x + bar_width / 2, q3_male, label='Q3 Male', color='green', width=bar_width)
plt.bar(x + bar_width / 2, q3_female, bottom=q3_male, label='Q3 Female', color='yellow', width=bar_width)

plt.bar(x + bar_width * 1.5, q4_male, label='Q4 Male', color='purple', width=bar_width)
plt.bar(x + bar_width * 1.5, q4_female, bottom=q4_male, label='Q4 Female', color='orange', width=bar_width)

# Penyesuaian
plt.xlabel('Stores')
plt.ylabel('Population')
plt.title('Population by Gender and Store (Quarterly)')
plt.xticks(x, stores)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Legenda diletakkan di luar grafik

plt.tight_layout(rect=[0, 0, 1, 0.80])
plt.show()
