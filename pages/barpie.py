import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header("📊 Diagnosa Pasien - Bar Chart & Pie Chart")

# Load data
@st.cache_data
def load_data():
    bulan = ['JAN','FEB','MAR','APR','MEI','JUNI','JULI','AGUST','SEPT','OKT','NOV','DES']
    semua_data = []
    for b in bulan:
        df = pd.read_excel("data/hospital.xlsx", sheet_name=b, usecols="AA,J,AV,F", nrows=10, engine='openpyxl')
        df["Bulan"] = b
        semua_data.append(df)
    gabungan = pd.concat(semua_data)
    gabungan.columns = ['ADMISSION_DATE', 'SEX', 'DESKRIPSI_INACBG', 'UMUR_TAHUN', 'Bulan']
    gabungan['SEX'] = gabungan['SEX'].map({1: 'Laki-laki', 2: 'Perempuan'})
    return gabungan

df = load_data()

# Bar Chart Horizontal (Stacked Bar Chart berdasarkan Gender)
st.subheader("📌 Stacked Horizontal Bar Chart - Diagnosa per Gender (Bulan Terpilih)")
bulan_pilihan = st.selectbox("Pilih Bulan:", df['Bulan'].unique())

# Filter data sesuai bulan
df_bulan = df[df['Bulan'] == bulan_pilihan]

# Kelompokkan data berdasarkan Diagnosa dan Gender
grouped = df_bulan.groupby(['DESKRIPSI_INACBG', 'SEX']).size().unstack(fill_value=0)

# Pastikan urutan diagnosa berdasarkan total jumlah kasus
grouped = grouped.sort_values(by=list(grouped.columns), ascending=False)

# Plot
fig1, ax1 = plt.subplots(figsize=(10, 6))
bottom = [0] * len(grouped)

colors = {
    'Laki-laki': '#007ACC',   # biru terang
    'Perempuan': '#FF69B4'    # pink
}

for gender in grouped.columns:
    ax1.barh(grouped.index, grouped[gender], left=bottom, label=gender, color=colors[gender])
    bottom = [i + j for i, j in zip(bottom, grouped[gender])]

ax1.set_xlabel("Jumlah Kasus")
ax1.set_title(f"Stacked Bar Diagnosa Pasien - Bulan {bulan_pilihan}")
ax1.legend(title="Gender")
ax1.invert_yaxis()
st.pyplot(fig1)


# Pie Chart
st.subheader("📌 Pie Chart - Persentase Diagnosa per Gender dan Bulan")
col1, col2 = st.columns(2)
with col1:
    bulan_pie = st.selectbox("Pilih Bulan Pie Chart:", df['Bulan'].unique(), key="pie_bulan")
with col2:
    gender_pie = st.selectbox("Pilih Gender Pie Chart:", df['SEX'].unique(), key="pie_gender")

df_pie = df[(df['Bulan'] == bulan_pie) & (df['SEX'] == gender_pie)]
jumlah_diagnosa = df_pie['DESKRIPSI_INACBG'].value_counts()

fig2, ax2 = plt.subplots(figsize=(7, 7))
ax2.pie(
    jumlah_diagnosa,
    labels=jumlah_diagnosa.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=plt.cm.Paired.colors
)
ax2.set_title(f"Pie Chart - {gender_pie}, {bulan_pie}")
st.pyplot(fig2)
