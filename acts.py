import streamlit as st

st.set_page_config(page_title="📦 Métricas logísticas", layout="centered")
import pandas as pd
import numpy as np

st.title("🚛 Dashboard Logístico Personalizado")
st.write("Este tema visual fue definido desde el archivo `.streamlit/config.toml` 🎨")

# Simulación simple de datos
data = pd.DataFrame(np.random.randn(20, 3), columns=['Tiempo', 'Retrasos', 'Entregas'])
st.line_chart(data)

# Slider de prueba visual
num = st.sidebar.slider("Selecciona un valor", 0, 100, 50)
st.write("📊 Valor seleccionado:", num)


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




st.header("🧠 Cuestionario con Selección Múltiple (`st.multiselect`)")

# Pregunta 1: Películas favoritas
peliculas = st.multiselect(
    "🎬 ¿Qué géneros de películas te gustan más?",
    ['Acción', 'Comedia', 'Terror', 'Romance', 'Ciencia Ficción'],
    default=['Acción', 'Comedia']
)
st.write("🎥 Géneros elegidos:", peliculas)

# Pregunta 2: Actividades de fin de semana
actividades = st.multiselect(
    "🛋️ ¿Qué te gusta hacer los fines de semana?",
    ['Dormir', 'Ver series', 'Salir con amigos', 'Leer', 'Hacer ejercicio'],
    default=['Ver series', 'Salir con amigos']
)
st.write("📅 Actividades seleccionadas:", actividades)

# Pregunta 3: Tipos de música
musica = st.multiselect(
    "🎧 ¿Qué géneros musicales disfrutas?",
    ['Rock', 'Reggaetón', 'Pop', 'Clásica', 'Jazz'],
    default=['Pop', 'Reggaetón']
)
st.write("🎶 Tus géneros musicales favoritos:", musica)

# Pregunta 4: Lenguajes de programación preferidos
lenguajes = st.multiselect(
    "👨‍💻 ¿Qué lenguajes de programación prefieres?",
    ['Python', 'JavaScript', 'C++', 'Java', 'R'],
    default=['Python', 'JavaScript']
)
st.write("💻 Lenguajes elegidos:", lenguajes)

# Pregunta 5: Frutas favoritas
frutas = st.multiselect(
    "🍓 ¿Cuáles son tus frutas favoritas?",
    ['Fresa', 'Plátano', 'Manzana', 'Mango', 'Sandía'],
    default=['Mango', 'Fresa']
)
st.write("🍍 Frutas seleccionadas:", frutas)


st.header("📦 ¿Qué métricas quieres ver en el dashboard de entregas?")

st.write("Selecciona las métricas a mostrar:")

# Checkboxes para seleccionar métricas
on_time = st.checkbox("✅ Porcentaje de entregas a tiempo")
avg_delay = st.checkbox("⏱️ Promedio de días de retraso")
region_perf = st.checkbox("📍 Desempeño por región")
weight_cat = st.checkbox("⚖️ Análisis por categoría de peso")
weather_effect = st.checkbox("🌦️ Impacto del clima en entregas")

# Respuestas según lo que seleccione el usuario
if on_time:
    st.write("✔️ Mostrando gráfico de entregas a tiempo...")
if avg_delay:
    st.write("📉 Cargando tabla con días promedio de retraso...")
if region_perf:
    st.write("🗺️ Mapa de rendimiento por región en camino...")
if weight_cat:
    st.write("📦 Segmentación de entregas por categoría de peso activada.")
if weather_effect:
    st.write("🌧️ Consultando correlación entre clima y demoras logísticas...")


