import streamlit as st
st.set_page_config(page_title="⏳ Múltiples Barras de Progreso", layout="centered")
import time


st.title("⏳ Múltiples Barras de Progreso")

with st.expander("ℹ️ Acerca de esta app"):
    st.write("Esta app demuestra cómo puedes usar varias barras de progreso en Streamlit que avancen a diferentes velocidades usando `st.progress`.")

# Crear 3 barras
bar1 = st.progress(0)
bar2 = st.progress(0)
bar3 = st.progress(0)

st.write("🚀 Avanzando tareas...")

# Simular progreso independiente
for i in range(101):
    # Barra rápida (sin pausa)
    if i <= 100:
        bar1.progress(i)

    # Barra media (pausa corta)
    if i <= 100:
        time.sleep(0.02)
        bar2.progress(i)

    # Barra lenta (pausa más larga)
    if i <= 100:
        time.sleep(0.03)
        bar3.progress(i)

st.success("🎉 ¡Todas las tareas han terminado!")
st.balloons()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuración del layout

st.title("🧩 Layout Streamlit con 5 Secciones")

# 📌 Sección 1: Expander con información
with st.expander("ℹ️ Acerca de esta app"):
    st.write("Esta app muestra cómo usar distintos elementos de layout para organizar una interfaz limpia y poderosa con Streamlit.")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=250)

# 📌 Sección 2: Inputs en la barra lateral
st.sidebar.header("📋 Entradas del usuario")
nombre = st.sidebar.text_input("¿Cuál es tu nombre?")
nivel = st.sidebar.slider("Nivel de satisfacción con esta app (1-10)", 1, 10, 5)
opcion = st.sidebar.selectbox("¿Qué módulo te gustó más?", ["", "Gráficos", "Expander", "Multiselect", "Sidebar"])
mostrar_tabla = st.sidebar.checkbox("¿Mostrar tabla de datos?")

# 📌 Sección 3: Datos en columnas
st.header("📊 Resultados personalizados")
col1, col2, col3 = st.columns(3)

with col1:
    if nombre:
        st.success(f"👋 ¡Hola, {nombre}!")
    else:
        st.warning("👈 Por favor ingresa tu **nombre** en la barra lateral.")

with col2:
    st.info(f"🔢 Nivel de satisfacción: **{nivel}/10**")

with col3:
    if opcion != "":
        st.write(f"✅ Te gustó más: **{opcion}**")
    else:
        st.write("👈 Elige un módulo que te haya gustado más.")

# 📌 Sección 4: Visualización de datos
st.subheader("📈 Visualización de datos simulados")
data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(data)

# 📌 Sección 5: Tabla expandible
if mostrar_tabla:
    with st.expander("🧮 Ver tabla completa"):
        st.dataframe(data.describe())

st.title('📤 Carga de múltiples archivos CSV')
st.write("Sube dos archivos distintos para analizarlos en la app.")

# Primer archivo
st.subheader('📦 Archivo de entregas')
entregas_file = st.file_uploader("Sube el archivo de entregas", type=['csv'], key="entregas")

if entregas_file is not None:
    df_entregas = pd.read_csv(entregas_file)
    st.write("✅ Entregas - Vista previa:")
    st.dataframe(df_entregas)
    st.write("📊 Estadísticas del archivo de entregas:")
    st.write(df_entregas.describe())
else:
    st.info("☝️ Sube un archivo CSV con información de entregas.")

# Segundo archivo
st.subheader('👥 Archivo de clientes')
clientes_file = st.file_uploader("Sube el archivo de clientes", type=['csv'], key="clientes")

if clientes_file is not None:
    df_clientes = pd.read_csv(clientes_file)
    st.write("✅ Clientes - Vista previa:")
    st.dataframe(df_clientes)
    st.write("📊 Estadísticas del archivo de clientes:")
    st.write(df_clientes.describe())
else:
    st.info("☝️ Sube un archivo CSV con información de clientes.")



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


