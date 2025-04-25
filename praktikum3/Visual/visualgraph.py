import streamlit as st
import graphviz as graphviz

st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")

st.title("GraphViz")
#Graph Obkect
st.graphviz_chart('''
digraph {
    "Training Data" -> "ML Algorithm"  
    "ML Algorithm" -> "Model"
    "Model" -> "Result Forecasting"
    "New Data" -> "Model"                
}
''')

st.write("")
st.write("")

# Create a graphlib graph object
st.title("Graphlib Graph Object")

graph = graphviz.Digraph()
graph.edge('Training Data', 'ML Algrorithm')
graph.edge('ML Algorithm', 'Model')
graph.edge('Model', 'Result Forecasting')
graph.edge('New Data', 'Model')
st.graphviz_chart(graph)
