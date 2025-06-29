import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.header("📊 Visualisasi Diagnosis Pasien - Bar Chart & Pie Chart")
st.markdown("Bagian ini menampilkan distribusi diagnosis pasien.")

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

available_months = df['Bulan'].unique().tolist()


# --- Bar Chart Horizontal (Stacked Bar Chart berdasarkan Gender) ---
st.subheader("📌 Stacked Bar Chart: Distribusi Diagnosa per Gender")
st.markdown("Visualisasi ini menunjukkan jumlah kasus untuk setiap diagnosis, dipisahkan berdasarkan jenis kelamin, dalam bulan yang dipilih.")

bulan_pilihan_bar = st.selectbox("Pilih Bulan untuk Bar Chart:", available_months, key="bar_month_select")

df_bulan_bar = df[df['Bulan'] == bulan_pilihan_bar].copy()

if df_bulan_bar.empty:
    st.warning(f"Tidak ada data diagnosa untuk bulan **{bulan_pilihan_bar}**.")
else:
    grouped_data = df_bulan_bar.groupby(['DESKRIPSI_INACBG', 'SEX']).size().unstack(fill_value=0)

    grouped_data['Total'] = grouped_data.sum(axis=1)
    grouped_data = grouped_data.sort_values(by='Total', ascending=False).drop(columns='Total')

    top_n_diagnoses_bar = st.slider("Jumlah Diagnosa Teratas untuk Bar Chart:", 5, 30, 15, key="bar_top_n_slider")
    if len(grouped_data) > top_n_diagnoses_bar:
        grouped_data = grouped_data.head(top_n_diagnoses_bar)

    if grouped_data.empty:
        st.info(f"Tidak ada diagnosis yang ditemukan untuk bulan **{bulan_pilihan_bar}** setelah penyaringan jumlah teratas.")
    else:
        fig1, ax1 = plt.subplots(figsize=(10, max(6, len(grouped_data) * 0.5)))

        colors = {
            'Laki-laki': '#1f77b4',
            'Perempuan': '#ff7f0e'
        }

        bottom_offset = [0] * len(grouped_data)
        
        for gender in ['Laki-laki', 'Perempuan']:
            if gender in grouped_data.columns:
                bars = ax1.barh(grouped_data.index, grouped_data[gender], left=bottom_offset, 
                                label=gender, color=colors.get(gender, 'gray'))
                
                for bar in bars:
                    width = bar.get_width()
                    if width > 0:
                        ax1.text(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2,
                                f'{int(width)}', va='center', ha='center', color='white', fontsize=7,
                                bbox=dict(facecolor='black', alpha=0.5, edgecolor='none', pad=1))
                bottom_offset = [i + j for i, j in zip(bottom_offset, grouped_data[gender])]

        ax1.set_xlabel("Jumlah Kasus")
        ax1.set_ylabel("Deskripsi Diagnosis")
        ax1.set_title(f"Stacked Bar Diagnosa Pasien - Bulan {bulan_pilihan_bar} (Top {top_n_diagnoses_bar})")
        ax1.legend(title="Gender")
        ax1.invert_yaxis()
        
        plt.tight_layout()
        st.pyplot(fig1, use_container_width=False)


# --- Pie Chart ---
st.subheader("📌 Pie Chart: Persentase Diagnosa per Gender dan Bulan")
st.markdown("Visualisasi ini menunjukkan proporsi diagnosis teratas dalam bentuk persentase untuk jenis kelamin dan bulan yang dipilih.")

col1, col2 = st.columns(2)
with col1:
    bulan_pie = st.selectbox("Pilih Bulan untuk Pie Chart:", available_months, key="pie_month_select")
with col2:
    gender_pie = st.selectbox("Pilih Gender untuk Pie Chart:", df['SEX'].unique(), key="pie_gender_select")

df_pie_filtered = df[(df['Bulan'] == bulan_pie) & (df['SEX'] == gender_pie)].copy()

if df_pie_filtered.empty:
    st.warning(f"Tidak ada data diagnosa untuk **{gender_pie}** pada bulan **{bulan_pie}**.")
else:
    jumlah_diagnosa_pie = df_pie_filtered['DESKRIPSI_INACBG'].value_counts()

    top_n_pie = st.slider("Jumlah Diagnosa Teratas untuk Pie Chart (sisanya 'Lainnya'):", 3, 15, 7, key="pie_top_n_slider")
    
    if len(jumlah_diagnosa_pie) > top_n_pie:
        top_diagnoses = jumlah_diagnosa_pie.head(top_n_pie - 1)
        other_count = jumlah_diagnosa_pie.iloc[top_n_pie - 1:].sum()
        final_diagnoses_for_pie = pd.concat([top_diagnoses, pd.Series({'Lainnya': other_count})])
    else:
        final_diagnoses_for_pie = jumlah_diagnosa_pie

    fig2, ax2 = plt.subplots(figsize=(12, 12)) 
    wedges, texts, autotexts = ax2.pie(
        final_diagnoses_for_pie,
        labels=final_diagnoses_for_pie.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=sns.color_palette("pastel", n_colors=len(final_diagnoses_for_pie)),
        pctdistance=0.85
    )
    ax2.set_title(f"Distribusi Diagnosa untuk {gender_pie} pada Bulan {bulan_pie}")
    ax2.axis('equal')

    ax2.legend(wedges, final_diagnoses_for_pie.index,
            title="Diagnosa",
            loc="center left",
            bbox_to_anchor=(0.9, 0.9))

    plt.tight_layout()
    st.pyplot(fig2, use_container_width=False)
