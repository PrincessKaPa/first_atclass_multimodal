import streamlit as st
from PIL import Image

import os
import time
import glob
import os

from gtts import gTTS
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

st.title("Interfases Multimodales.")
image = Image.open('text_to_audio.png')

st.image(image, width=200)


try:
    os.mkdir("temp")
except:
    pass

st.subheader("Texto a audio.")
st.write('Las interfaces de texto a audio son fundamentales en las interfaces multimodales ya que permiten '  
         'una comunicación más accesible y natural, facilitando la inclusión de personas con discapacidades ' 
         ' visuales y permitiendo la interacción en situaciones donde no es posible leer texto. Estas interfaces '  
         ' también impulsan tecnologías emergentes como los asistentes de voz inteligentes, haciendo que la tecnología ' 
         ' sea más accesible e intuitiva para todos los usuarios')
           

text = st.text_input("Ingrese el texto.")

tld="es"

def text_to_speech(text, tld):
    
    tts = gTTS(text,"es", tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text


#display_output_text = st.checkbox("Verifica el texto")

if st.button("convertir"):
    result, output_text = text_to_speech(text, tld)
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown(f"## Tú audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    #if display_output_text:
    st.markdown(f"## Texto en audio:")
    st.write(f" {output_text}")


def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)
