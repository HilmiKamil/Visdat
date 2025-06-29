import streamlit as st

st.set_page_config(
    page_title="Aplikasi Visualisasi Diagnosis Pasien",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Aplikasi Visualisasi Diagnosis Pasien - RS Harapan Bunda")

st.markdown("""
**Disusun oleh:**
- **Ilyas Abdul Aziz** – 0110223292
- **Muhamad Hilmi Kamil** – 0110223293
- **Ferisha Adilla Hidayat** – 0110223286
- **Kelas:** 4SE02 (Kelompok 9) – Kamis, 13.00–15.00
""")

st.info("Silakan pilih menu di sidebar untuk mengeksplorasi visualisasi data diagnosis pasien.")

st.markdown("""
Aplikasi ini dirancang untuk memvisualisasikan data diagnosis pasien dari RS Harapan Bunda
selama periode Oktober hingga Desember, untuk memberikan wawasan mengenai pola penyakit,
distribusi berdasarkan jenis kelamin dan usia, serta tren bulanan.
""")

st.markdown("""
**Sumber Data:** Data internal RS Harapan Bunda.
""")