import streamlit as st

st.subheader("Kelompok 9 Visualisasi Data:")

#Markdown (Membuat List Nama)

st.markdown("""
- Ilyas Abdul Aziz - 0110223292
- Muhamad Hilmi Kamil - 0110223293
- Ferisha Adilla Hidayat - 0110223286
""")

st.write("")
st.write("")

st.write("Selamat datang di halaman visualisasi data kami!")
st.title("Explore the Power of Data!!!")
st.header("Transforming Data into Meaningful Insights")
st.subheader("Bersama kami, data berbicara lebih banyak!")
st.caption("This is our Captain: guiding us through the data journey")

#Plain Text
st.text("Hi, \nPeople\t!!!!!!")
st.text('Welcome to')
st.text("Streamlit's  World")

#Markdown
st.markdown("#Hi, \n# ***People*** \t!!!!!!")
st.markdown('## Welcome to')
st.markdown("""### Streamlit's World""")

#Latex
st.latex(r'''cos2\theta = 1 - 2sin^2\theta''')
st.latex("""(a+b)^2 = a^2 + b^2 + 2ab""")
st.latex(r'''\frac{\partial u}{\partial t}
        = h^2 \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2}
        + \frac{\partial^2 u}{\partial z^2} \right)
        ''')

#Python Code
st.subheader("Python Code")
code = '''def hello();
print("Hello streamlit!")'''
st.code(code, language='python')

#Java Code
st.subheader("Java Code")
st.code("""Public Class GFG {
public static void main(String args[])
{
    System.out.println("Hello World");
}
}""", language='javascript')
st.subheader("Javascript Code")
st.code(""" <p id="demo"></p>
        <script>
        try {
        addlert("Welcome guest!");
        }
        catch(err) {
        document.getElementById("demo").innerHTML = err.message;
        }
        </script>""")




