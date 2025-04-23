# Dataframe using magic
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")

# Math calculations with no functions defined
"Adding 5 & 4 =", 5 + 4

# Displaying Variable 'a' and its value
a = 5
'a', a

# Markdown with Magic
"""
# Magic Feature
Markdown working without defining its function explicitly.
"""

df = pd.DataFrame({'col': [1, 2]})
'dataframe', df

# Magic working on Charts


s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)

# Magic chart
"chart", chart