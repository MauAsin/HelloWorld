import streamlit as st

st.set_page_config(page_title="🧠 Cuestionario Interactivo", layout="centered")
st.header("🧠 Cuestionario rápido con `st.selectbox`")

# Pregunta 1: Color favorito
color = st.selectbox(
    "🎨 ¿Cuál es tu color favorito?",
    ('Azul', 'Rojo', 'Verde', 'Negro', 'Amarillo')
)
st.write("🖌️ Elegiste:", color)

# Pregunta 2: Comida favorita
comida = st.selectbox(
    "🍕 ¿Qué comida prefieres?",
    ('Pizza', 'Tacos', 'Sushi', 'Hamburguesa', 'Ensalada')
)
st.write("🍽️ Te gusta:", comida)

# Pregunta 3: Deporte favorito
deporte = st.selectbox(
    "🏀 ¿Cuál es tu deporte favorito?",
    ('Fútbol', 'Básquetbol', 'Tenis', 'Beisbol', 'Natación')
)
st.write("⚽ Practicas o disfrutas:", deporte)

# Pregunta 4: Lugar para vacacionar
lugar = st.selectbox(
    "🏖️ ¿Dónde te gustaría vacacionar?",
    ('Playa', 'Montaña', 'Ciudad', 'Selva', 'Desierto')
)
st.write("🌍 Tu lugar ideal es:", lugar)

# Pregunta 5: Superpoder deseado
poder = st.selectbox(
    "🦸‍♂️ ¿Qué superpoder tendrías?",
    ('Volar', 'Leer mentes', 'Ser invisible', 'Teletransportarte', 'Super fuerza')
)
st.write("💥 Tu superpoder elegido es:", poder)
