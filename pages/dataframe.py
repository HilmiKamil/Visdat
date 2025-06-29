import streamlit as st
import pandas as pd

st.header("📋 Data Pasien (Preview & Eksplorasi)")

@st.cache_data
def load_and_clean_data():
    bulan = ['OKT', 'NOV', 'DES']
    all_data = []

    for b in bulan:
        df = pd.read_excel("data/hospital.xlsx", sheet_name=b, usecols="AA,J,AV,F", engine='openpyxl')
        df["Bulan"] = b
        all_data.append(df)

    combined_df = pd.concat(all_data)
    combined_df.columns = ['ADMISSION_DATE', 'SEX', 'DESKRIPSI_INACBG', 'UMUR_TAHUN', 'Bulan']
    combined_df['SEX'] = combined_df['SEX'].map({1: 'Laki-laki', 2: 'Perempuan'})
    
    initial_rows = len(combined_df)
    combined_df.dropna(subset=['DESKRIPSI_INACBG', 'SEX', 'UMUR_TAHUN', 'ADMISSION_DATE'], inplace=True)
    combined_df.drop_duplicates(inplace=True)
    combined_df['ADMISSION_DATE'] = pd.to_datetime(combined_df['ADMISSION_DATE'], errors='coerce')
    combined_df.dropna(subset=['ADMISSION_DATE'], inplace=True)

    st.sidebar.success(f"Data bersih dimuat: {len(combined_df)} dari {initial_rows} baris.")
    
    return combined_df

df = load_and_clean_data()

st.success(f"Total Data yang Dimuat: {len(df)} Baris")

with st.expander("📌 Lihat Data Mentah (Preview 10000 Baris Pertama)"):
    st.dataframe(df.head(10000))
    st.write(f"Menampilkan {min(10900, len(df))} baris pertama dari total {len(df)} baris.")

st.markdown("""
**Deskripsi Kolom:**
- `ADMISSION_DATE`: Tanggal masuk pasien.
- `SEX`: Jenis kelamin pasien (Laki-laki/Perempuan).
- `DESKRIPSI_INACBG`: Deskripsi diagnosis.
- `UMUR_TAHUN`: Umur pasien dalam tahun.
- `Bulan`: Bulan data (Oktober, November, Desember).
""")