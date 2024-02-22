import streamlit as st
from PIL import Image

st.title("¡Mi primera app!!") #Una app web que solo muestra un tìtulo
st.title("DrEaMiNg")

st.header("Un espacio para crear y soñar")
st.write("Utilizo esta app para crear fàcil y ràpidamente frondend y backend")
image = Image.open('nubesmoradas.jpeg')

st.image(image, caption="nubes moradas")




