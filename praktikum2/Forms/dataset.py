import streamlit as st
import pandas as pd

st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")


st.title("CSV Data")
data_file = st.file_uploader("Upload CSV", type=["csv"])
details = st.button("Check Details")

if details:
    if data_file is not None:
        file_details = {
            "file_name": data_file.name,
            "file_type": data_file.type,
            "file_size": data_file.size
        }
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")