import streamlit as st
import pandas as pd

st.header("📋 Data Pasien (Preview & Eksplorasi)")

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

with st.expander("📌 Lihat Data Mentah"):
    st.dataframe(df.head(20))

st.success(f"Total Data: {len(df)} Baris")
