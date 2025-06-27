import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.header("📈 Line Chart & Heatmap")

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

# --- Line Chart ---
st.subheader("📈 Tren Bulanan Diagnosa Tertentu")
diagnosa = st.selectbox("Pilih Diagnosa:", df['DESKRIPSI_INACBG'].unique())
df_line = df[df['DESKRIPSI_INACBG'] == diagnosa]
line_data = df_line.groupby(['Bulan', 'SEX']).size().unstack(fill_value=0)

fig1, ax1 = plt.subplots()
line_data.plot(marker='o', ax=ax1)
ax1.set_ylabel("Jumlah Kasus")
ax1.set_title(f"Tren Bulanan Diagnosa: {diagnosa}")
st.pyplot(fig1)

# --- Heatmap ---
st.subheader("🌡️ Heatmap Diagnosa vs Gender")
heat_data = df.groupby(['DESKRIPSI_INACBG', 'SEX']).size().unstack(fill_value=0)
fig2, ax2 = plt.subplots(figsize=(10, len(heat_data)*0.4))
sns.heatmap(heat_data, annot=True, fmt='d', cmap="YlGnBu", ax=ax2)
ax2.set_title("Jumlah Kasus per Diagnosa & Gender")
st.pyplot(fig2)
