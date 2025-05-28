import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Gabungkan Data dari Semua Bulan ---
all_data = []

for month in ['JAN', 'FEB', 'MAR', 'APR', 'MEI', 'JUNI', 'JULI', 'AGUST', 'SEPT', 'OKT', 'NOV', 'DES']:
    df_month = pd.read_excel(
        io="hospital.xlsx",
        engine="openpyxl",
        sheet_name=month,
        usecols="AA, J, AV, F",
        nrows=1000
    )
    df_month["Bulan"] = month
    all_data.append(df_month)

df = pd.concat(all_data)
df.columns = ['ADMISSION_DATE', 'SEX', 'DESKRIPSI_INACBG', 'UMUR_TAHUN', 'Bulan']
df['SEX'] = df['SEX'].map({1: 'Laki-laki', 2: 'Perempuan'})

# --- Judul Aplikasi ---
st.title("Visualisasi Diagnosa Berdasarkan Usia dan Jenis Kelamin (Jan–Des)")

# --- Filter Data ---
selected_bulan = st.multiselect("Pilih Bulan:", df['Bulan'].unique(), default=df['Bulan'].unique())
selected_diagnosa = st.multiselect("Pilih Diagnosa:", df['DESKRIPSI_INACBG'].unique()[:10], default=df['DESKRIPSI_INACBG'].unique()[:5])
selected_gender = st.multiselect("Pilih Gender:", df['SEX'].unique(), default=df['SEX'].unique())

filtered_df = df[
    (df['Bulan'].isin(selected_bulan)) &
    (df['DESKRIPSI_INACBG'].isin(selected_diagnosa)) &
    (df['SEX'].isin(selected_gender))
]

# --- Tabel Data yang Difilter ---
st.dataframe(filtered_df)

# --- Bar Chart: Jumlah Kasus per Diagnosa dan Gender ---
st.subheader("Bar Chart: Jumlah Kasus per Diagnosa dan Gender")

grouped = filtered_df.groupby(['DESKRIPSI_INACBG', 'SEX']).size().unstack(fill_value=0)
fig1, ax1 = plt.subplots(figsize=(12, 6))
grouped.plot(kind='bar', ax=ax1)
ax1.set_title("Jumlah Kasus Diagnosa Berdasarkan Gender")
ax1.set_xlabel("Diagnosa")
ax1.set_ylabel("Jumlah Kasus")
ax1.legend(title="Gender")
plt.xticks(rotation=45, ha='right')
st.pyplot(fig1)

# --- Line Chart: Tren Bulanan Kasus Berdasarkan Gender ---
st.subheader("Line Chart: Tren Bulanan Kasus Berdasarkan Gender")

selected_diagnosa_line = st.selectbox("Pilih Diagnosa untuk Lihat Tren Bulanannya:", grouped.index)
df_line = filtered_df[filtered_df['DESKRIPSI_INACBG'] == selected_diagnosa_line]
line_data = df_line.groupby(['Bulan', 'SEX']).size().unstack(fill_value=0)
line_data = line_data.reindex(index=['JAN', 'FEB', 'MAR', 'APR', 'MEI', 'JUNI', 'JULI', 'AGUST', 'SEPT', 'OKT', 'NOV', 'DES'])

fig2, ax2 = plt.subplots(figsize=(10, 5))
line_data.plot(kind='line', marker='o', ax=ax2)
ax2.set_title(f"Tren Bulanan untuk Diagnosa: {selected_diagnosa_line}")
ax2.set_xlabel("Bulan")
ax2.set_ylabel("Jumlah Kasus")
ax2.legend(title="Gender")
plt.xticks(rotation=45)
st.pyplot(fig2)

# --- Heatmap: Jumlah Kasus per Diagnosa dan Gender ---
st.subheader("Heatmap: Jumlah Kasus per Diagnosa dan Gender")

heatmap_data = filtered_df.groupby(['DESKRIPSI_INACBG', 'SEX']).size().unstack(fill_value=0)
fig3, ax3 = plt.subplots(figsize=(12, len(heatmap_data) * 0.5))
sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="YlGnBu", ax=ax3)
ax3.set_title("Jumlah Kasus Diagnosa per Gender")
ax3.set_xlabel("Gender")
ax3.set_ylabel("Diagnosa")
st.pyplot(fig3)

# --- Scatter Plot: Umur vs Jenis Penyakit dengan Warna Gender ---
st.subheader("Scatter Plot: Umur vs Jenis Penyakit dengan Warna Gender")

fig4, ax4 = plt.subplots(figsize=(12, 6))
colors = {'Laki-laki': 'blue', 'Perempuan': 'red'}

for gender in filtered_df['SEX'].unique():
    subset = filtered_df[filtered_df['SEX'] == gender]
    ax4.scatter(subset['UMUR_TAHUN'], subset['DESKRIPSI_INACBG'], label=gender, alpha=0.6, c=colors[gender])

ax4.set_title("Penyebaran Umur Pasien Berdasarkan Jenis Penyakit dan Gender")
ax4.set_xlabel("Umur (Tahun)")
ax4.set_ylabel("Jenis Penyakit (Diagnosa)")
ax4.legend(title="Gender")
plt.xticks(rotation=45)
plt.grid(True)
st.pyplot(fig4)

# --- Pie Chart: Persentase Diagnosa ---
st.subheader("Pie Chart: Persentase Diagnosa")

diagnosa_counts = filtered_df['DESKRIPSI_INACBG'].value_counts()
fig5, ax5 = plt.subplots(figsize=(8, 8))
ax5.pie(diagnosa_counts, labels=diagnosa_counts.index, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 8})
ax5.axis('equal')
plt.title("Distribusi Diagnosa Berdasarkan Jumlah Pasien", fontsize=12, fontweight='bold')
st.pyplot(fig5)

