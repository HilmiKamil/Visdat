import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.header("📈 Line Chart & Heatmap")
st.markdown("Bagian ini menampilkan tren jumlah kasus diagnosis dari waktu ke waktu dan korelasi antara diagnosis dan jenis kelamin.")

@st.cache_data
def load_and_clean_data():
    """
    Memuat data pasien dari file Excel dan melakukan pembersihan.
    """
    bulan = ['OKT', 'NOV', 'DES']
    all_data = []

    for b in bulan:
        df = pd.read_excel("data/hospital.xlsx", sheet_name=b, usecols="AA,J,AV,F", engine='openpyxl')
        df["Bulan"] = b
        all_data.append(df)

    combined_df = pd.concat(all_data)
    combined_df.columns = ['ADMISSION_DATE', 'SEX', 'DESKRIPSI_INACBG', 'UMUR_TAHUN', 'Bulan']
    combined_df['SEX'] = combined_df['SEX'].map({1: 'Laki-laki', 2: 'Perempuan'})
    
    # Proses Pembersihan Data
    initial_rows = len(combined_df)
    combined_df.dropna(subset=['DESKRIPSI_INACBG', 'SEX', 'UMUR_TAHUN', 'ADMISSION_DATE'], inplace=True)
    combined_df.drop_duplicates(inplace=True)
    combined_df['ADMISSION_DATE'] = pd.to_datetime(combined_df['ADMISSION_DATE'], errors='coerce')
    combined_df.dropna(subset=['ADMISSION_DATE'], inplace=True) # Hapus jika konversi tanggal gagal

    st.sidebar.success(f"Data bersih dimuat: {len(combined_df)} dari {initial_rows} baris.")
    
    return combined_df

df = load_and_clean_data()

# --- Line Chart ---
st.subheader("📈 Tren Bulanan Diagnosa Tertentu")
st.markdown("Visualisasi ini menunjukkan bagaimana jumlah kasus untuk diagnosis tertentu berubah dari bulan ke bulan.")

available_diagnoses = df['DESKRIPSI_INACBG'].unique().tolist()

if not available_diagnoses:
    st.warning("Tidak ada diagnosa yang tersedia untuk ditampilkan.")
else:
    diagnosa_terpilih = st.selectbox("Pilih Diagnosa:", available_diagnoses)
    
    df_line = df[df['DESKRIPSI_INACBG'] == diagnosa_terpilih].copy()
    
    # Urutkan bulan secara kronologis
    bulan_order = ['OKT', 'NOV', 'DES']
    df_line['Bulan'] = pd.Categorical(df_line['Bulan'], categories=bulan_order, ordered=True)
    
    line_data = df_line.groupby(['Bulan', 'SEX']).size().unstack(fill_value=0)
    
    if line_data.empty:
        st.info(f"Tidak ada data tren untuk diagnosa: **{diagnosa_terpilih}**.")
    else:
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        line_data.plot(marker='o', ax=ax1, cmap='viridis')
        ax1.set_xlabel("Bulan")
        ax1.set_ylabel("Jumlah Kasus")
        ax1.set_title(f"Tren Bulanan Diagnosa: {diagnosa_terpilih}")
        ax1.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        st.pyplot(fig1, use_container_width=False)


# --- Heatmap ---
st.subheader("🌡️ Heatmap Diagnosa vs Gender")
st.markdown("Heatmap ini menunjukkan intensitas kasus untuk setiap diagnosis berdasarkan jenis kelamin.")

# Filter untuk top N diagnosa agar heatmap tidak terlalu panjang
top_n_diagnoses_heatmap = st.slider("Jumlah Diagnosa Teratas untuk Heatmap:", 5, 20, 15, key="heatmap_top_n_slider")
diagnosis_counts_heatmap = df['DESKRIPSI_INACBG'].value_counts()
top_diagnoses_list_heatmap = diagnosis_counts_heatmap.head(top_n_diagnoses_heatmap).index.tolist()

df_heatmap_filtered = df[df['DESKRIPSI_INACBG'].isin(top_diagnoses_list_heatmap)].copy()

if df_heatmap_filtered.empty:
    st.warning(f"Tidak ada data yang cukup untuk menampilkan heatmap (mungkin semua diagnosis di luar top {top_n_diagnoses_heatmap}).")
else:
    heat_data = df_heatmap_filtered.groupby(['DESKRIPSI_INACBG', 'SEX']).size().unstack(fill_value=0)

    # Urutkan data heatmap berdasarkan total kasus untuk konsistensi
    heat_data['Total'] = heat_data.sum(axis=1)
    heat_data = heat_data.sort_values(by='Total', ascending=False).drop(columns='Total')
    
    fig2, ax2 = plt.subplots(figsize=(12, max(7, len(heat_data)*0.5))) # Ukuran fig disesuaikan secara dinamis
    sns.heatmap(heat_data, annot=True, fmt='d', cmap="YlGnBu", ax=ax2, linewidths=.5, linecolor='black')
    ax2.set_title(f"Jumlah Kasus per Diagnosa & Gender (Top {top_n_diagnoses_heatmap} Diagnosa)")
    ax2.set_xlabel("Gender")
    ax2.set_ylabel("Diagnosa")
    plt.tight_layout()
    st.pyplot(fig2, use_container_width=False)