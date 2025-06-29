import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header("🔍 Scatter Plot: Umur vs Diagnosa")
st.markdown("Bagian ini menampilkan hubungan antara umur pasien dan diagnosis mereka.")

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

selected_gender = st.radio("Pilih Gender untuk Analisis Umur vs Diagnosa:", df['SEX'].unique())
filtered_df_by_gender = df[df['SEX'] == selected_gender].copy()

if filtered_df_by_gender.empty:
    st.warning(f"Tidak ada data untuk gender: **{selected_gender}**.")
else:
    st.subheader(f"Scatter Plot: Distribusi Umur Pasien ({selected_gender}) per Diagnosa")
    st.markdown("Setiap titik mewakili satu pasien, menunjukkan umur mereka dan diagnosis yang mereka terima.")

    top_n_scatter = st.slider("Jumlah Diagnosa Teratas untuk Scatter Plot:", 5, 20, 10, key="scatter_top_n_slider")
    
    diagnosis_counts_scatter = filtered_df_by_gender['DESKRIPSI_INACBG'].value_counts()
    top_diagnoses_list_scatter = diagnosis_counts_scatter.head(top_n_scatter).index.tolist()
    filtered_for_scatter = filtered_df_by_gender[filtered_df_by_gender['DESKRIPSI_INACBG'].isin(top_diagnoses_list_scatter)].copy()

    if filtered_for_scatter.empty:
        st.info("Tidak ada data yang cukup untuk scatter plot setelah penyaringan diagnosa teratas.")
    else:
        fig_scatter, ax_scatter = plt.subplots(figsize=(12, 7))
        ax_scatter.scatter(filtered_for_scatter['UMUR_TAHUN'], filtered_for_scatter['DESKRIPSI_INACBG'], 
                        alpha=0.7, s=30, color='skyblue', edgecolors='black')

        ax_scatter.set_title(f"Distribusi Umur Pasien ({selected_gender}) per Diagnosa (Top {top_n_scatter})")
        ax_scatter.set_xlabel("Umur (Tahun)")
        ax_scatter.set_ylabel("Diagnosa")
        ax_scatter.grid(True, linestyle='--', alpha=0.6)
        
        plt.tight_layout()
        st.pyplot(fig_scatter, use_container_width=False)