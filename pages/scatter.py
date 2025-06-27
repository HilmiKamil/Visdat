import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header("🔍 Scatter Plot: Umur vs Diagnosa")

@st.cache_data
def load_data():
    bulan = ['JAN','FEB','MAR','APR','MEI','JUNI','JULI','AGUST','SEPT','OKT','NOV','DES']
    all_data = []
    for b in bulan:
        df = pd.read_excel("data/hospital.xlsx", sheet_name=b, usecols="AA,J,AV,F", nrows=10, engine='openpyxl')
        df["Bulan"] = b
        all_data.append(df)
    df = pd.concat(all_data)
    df.columns = ['ADMISSION_DATE', 'SEX', 'DESKRIPSI_INACBG', 'UMUR_TAHUN', 'Bulan']
    df['SEX'] = df['SEX'].map({1: 'Laki-laki', 2: 'Perempuan'})
    return df

df = load_data()

selected_gender = st.radio("Pilih Gender:", df['SEX'].unique())
filtered = df[df['SEX'] == selected_gender]

fig, ax = plt.subplots(figsize=(12, 6))
ax.scatter(filtered['UMUR_TAHUN'], filtered['DESKRIPSI_INACBG'], alpha=0.7)
ax.set_title(f"Distribusi Umur Pasien ({selected_gender})")
ax.set_xlabel("Umur (Tahun)")
ax.set_ylabel("Diagnosa")
st.pyplot(fig)
