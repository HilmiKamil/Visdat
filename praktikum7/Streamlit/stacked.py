import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Streamlit layout
st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")

st.title("Stacked Vertical Bar Chart")

# Data
stores = ['Store A', 'Store B', 'Store C']
male_population = [150, 200, 180]
female_population = [120, 230, 170]

# Grafik
fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, male_population, label='Male', color='blue')
ax.bar(x, female_population, bottom=male_population, label='Female', color='pink')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_title('Population by Gender and Store')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

# Tampilkan di Streamlit
st.pyplot(fig)


st.subheader("Membuat Stacked Vertical Bar Chart dengan Matplotlib")

# Data Transaksi Penjualan
stores = ['Store A', 'Store B', 'Store C']
product_a_sales = [200, 250, 300]
product_b_sales = [150, 300, 250]

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, product_a_sales, label='Product A', color='blue')
ax.bar(x, product_b_sales, bottom=product_a_sales, label='Product B', color='green')

ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_title('Sales Transactions by Store')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

# Tampilkan di Streamlit
st.pyplot(fig)


st.subheader("Kustomisasi Stacked Vertical Bar Chart")

for i in range(len(x)):
    plt.text(x[i], product_a_sales[i] / 2, str(product_a_sales[i]), ha='center', color='white')
    plt.text(x[i], product_a_sales[i] + product_b_sales[i] / 2, str(product_b_sales[i]), ha='center', color='black')

st.pyplot(fig)

st.subheader("Multiple Stacked Vertical Bar Chart")

# Data tambahan
q1_male = [150, 180, 160]
q1_female = [140, 200, 180]
q2_male = [170, 190, 175]
q2_female = [130, 210, 160]

fig, ax = plt.subplots()
bar_width = 0.4
x = np.arange(len(stores))

ax.bar(x - bar_width / 2, q1_male, label='Q1 Male', color='lightblue', width=bar_width)
ax.bar(x - bar_width / 2, q1_female, bottom=q1_male, label='Q1 Female', color='pink', width=bar_width)
ax.bar(x + bar_width / 2, q2_male, label='Q2 Male', color='blue', width=bar_width)
ax.bar(x + bar_width / 2, q2_female, bottom=q2_male, label='Q2 Female', color='red', width=bar_width)

ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_title('Population by Gender and Store (Multiple Quarters)')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

st.pyplot(fig)
