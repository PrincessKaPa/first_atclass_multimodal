import streamlit as st
from PIL import Image

st.title("¡Mi primera app!!") #Una app web que solo muestra un tìtulo
st.title("DrEaMiNg")
st.header("Un espacio para crear y soñar")
st.write("Utilizo esta app para crear fàcil y ràpidamente frondend y backend")
image = Image.open('nubesmoradas.jpeg')

st.image(image, caption="nubes moradas")


texto = st.text_input("Escribe algo", "Este es mi texto")
st.write("Esto es lo que escribiste: ", texto)

st.subheader("Ahora usemos 2 columnas jeje")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Te presento la primera columna :)")
  st.write("Las interfaces multomodales mejoran la experiencia de usuario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("¡Correcto!")

with col2:
  st.subheader("Y aquí está la segunda columna ^^")
  modo = st.radio("¿Qué modalidad es la principal en tu interfaz?", ("Visual", "Auditiva", "Táctil"))
  if modo == "Visual":
    st.write("La vista es fundamental en tu interfaz")
  if modo == "Auditiva":
    st.write("La audición es fundamental para tu interfaz")
  if modo == "Táctil":
    st.write("El tacto es fundamental para tu interfaz")

st.subheader("Uso de botones")
if st.button("Presiona el botón"):
  st.write("Gracias por presionar")
else:
  st.write("No lo has presionado aún")
