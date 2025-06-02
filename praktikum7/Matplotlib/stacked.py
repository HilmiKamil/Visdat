import matplotlib.pyplot as plt
import numpy as np

# Membuat List Nama
plt.figtext(0.5, 0.92, "Kelompok 9 - Visualisasi Data", ha='center', fontsize=14, fontweight='bold')
plt.figtext(0.5, 0.80, "- Ilyas Abdul Aziz (0110223292)\n- Muhamad Hilmi Kamil (0110223293)\n- Ferisha Adilla Hidayat (0110223286)",
            ha='center', fontsize=10)

#Data

stores = ['Store A', 'Store B', 'Store C']
male_population = [150, 200, 180]
female_population = [120, 230, 170]

#Bar Position

x = np.arange(len(stores))

#Stacked Bar Chart

plt.bar(x, male_population, label='Male', color='blue')
plt.bar(x, female_population, bottom=male_population, label='Female', color='pink')

#Penyesuaian
plt.xlabel('Stores')
plt.ylabel('Population')
plt.title('Population by Gender and Store')
plt.xticks(x, stores)
plt.legend()

plt.tight_layout(rect=[0, 0, 1, 0.80])

#Show
plt.show()