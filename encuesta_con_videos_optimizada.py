
import streamlit as st
import pandas as pd
import numpy as np
import time

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(page_title="📝 Encuesta con contexto en video", layout="wide")
st.title("🧠 Encuesta de Opinión sobre el Servicio")

with st.expander("ℹ️ Acerca de esta encuesta"):
    st.write("Responde después de ver los videos. Tu opinión nos ayuda a mejorar.")

# --- VIDEO 1 ---
st.subheader("🎥 Video introductorio")
st.video("https://www.youtube.com/watch?v=2Xc9gXyf2G4")

# --- FORMULARIO DE ENCUESTA ---
with st.form("encuesta_formulario"):
    st.subheader("📋 Formulario de Opinión")
    nombre = st.text_input("1. ¿Cuál es tu nombre?")
    edad = st.slider("2. ¿Cuál es tu edad?", 18, 99, 25)
    genero = st.radio("3. ¿Con qué género te identificas?", ["Masculino", "Femenino", "Otro", "Prefiero no decir"])
    satisfaccion = st.slider("4. ¿Qué tan satisfecho estás con nuestro servicio?", 1, 10, 7)
    recomendar = st.radio("5. ¿Recomendarías nuestro servicio?", ["Sí", "No", "Tal vez"])
    frecuencia = st.selectbox("6. ¿Con qué frecuencia utilizas nuestro servicio?", ["Diario", "Semanal", "Mensual", "Ocasional", "Primera vez"])
    canal = st.selectbox("7. ¿Cómo conociste este servicio?", ["Redes sociales", "Publicidad", "Amigo/Familiar", "Otro"])
    opinion = st.text_area("8. ¿Qué fue lo que más te gustó?")
    mejora = st.text_area("9. ¿Qué podemos mejorar?")
    privacidad = st.checkbox("10. Acepto el uso de mis respuestas de forma anónima para mejorar el servicio.")
    enviado = st.form_submit_button("Enviar encuesta")

if enviado:
    st.success("✅ ¡Gracias por responder la encuesta!")
    st.markdown(f'''
    ### 🧾 Resumen:
    - **Nombre:** {nombre}
    - **Edad:** {edad}
    - **Género:** {genero}
    - **Satisfacción:** {satisfaccion}/10
    - **Recomienda:** {recomendar}
    - **Frecuencia:** {frecuencia}
    - **Canal:** {canal}
    - **Lo mejor:** {opinion}
    - **Sugerencias:** {mejora}
    - **Privacidad:** {"Sí" if privacidad else "No"}
    ''')

# --- VIDEO 2 ---
st.subheader("📽️ Video adicional (cierre)")
st.video("https://www.youtube.com/watch?v=jNQXAC9IVRw")
