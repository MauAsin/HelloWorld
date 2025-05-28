
# app2.py
import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# Configurar la página
st.write('Hello world!')

# Varios mensajes usando st.write()
st.write("👋 ¡Bienvenido a mi primera app con Streamlit!")
st.write("✅ Aquí aprenderás a usar `st.write()` de forma divertida.")
st.write("📊 Puedes combinar texto, emojis, e incluso variables de Python.")
st.write("🧠 Tip: `st.write()` es súper versátil y acepta casi cualquier cosa.")
st.write("🚀 ¡Ahora sí, listo para construir cosas más chingonas con Streamlit!")

# Botón con acción
st.header('st.button')
if st.button('Say hello'):
    st.write('Why hello there')  # <- esta línea debe estar indentada
else:
    st.write('Goodbye')          # <- esta también

st.title("🎮 App de los 3 Botones Misteriosos")

st.subheader("Botón 1 - Motivación")
if st.button("Haz clic aquí para motivarte"):
    st.write("💪 ¡Hoy es el día para romperla!")
else:
    st.write("ADIOS")

st.subheader("Botón 2 - Chisme tecnológico")
if st.button("Dame un dato geek"):
    st.write("🤖 ¿Sabías que el primer bug fue literalmente una polilla en una computadora en 1947?")
else:
    st.write("ADIOS")

st.subheader("Botón 3 - Consejo de vida")
if st.button("Un consejo random"):
    st.write("🧠 No tomes decisiones importantes con hambre, sueño o coraje.")
else:
    st.write("ADIOS")

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header('st.write')

# Example 1: Texto con markdown y emoji
st.write('Hello, *World!* :sunglasses:')

# Example 2: Un número
st.write(1234)

# Example 3: Un DataFrame simple
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

# Example 4: Texto + DataFrame combinado
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5: Gráfico interactivo con Altair
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)

c = alt.Chart(df2).mark_circle().encode(
    x='a',
    y='b',
    size='c',
    color='c',
    tooltip=['a', 'b', 'c']
)

st.write(c)

import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página

st.title("🌸 Dashboard interactivo del dataset Iris")

# Cargar el dataset Iris
df = sns.load_dataset("iris")

# Mostrar los primeros datos
st.subheader("📋 Vista previa del dataset")
st.dataframe(df)

# Histograma interactivo
st.subheader("📊 Histograma por columna")
num_cols = df.select_dtypes(include='number').columns.tolist()
col = st.selectbox("Selecciona una variable numérica", num_cols)

fig1, ax1 = plt.subplots()
ax1.hist(df[col], bins=20, color="mediumseagreen", edgecolor="black")
ax1.set_title(f"Distribución de {col}")
st.pyplot(fig1)

# Gráfico de dispersión interactivo
st.subheader("🌿 Gráfico de dispersión")
col_x = st.selectbox("Eje X", num_cols, key="x")
col_y = st.selectbox("Eje Y", num_cols, key="y")

fig2, ax2 = plt.subplots()
species = df['species'].unique()
for sp in species:
    subset = df[df['species'] == sp]
    ax2.scatter(subset[col_x], subset[col_y], label=sp)
ax2.set_xlabel(col_x)
ax2.set_ylabel(col_y)
ax2.legend()
ax2.set_title(f"Dispersión entre {col_x} y {col_y}")
st.pyplot(fig2)


from datetime import time, datetime

st.set_page_config(page_title="🕹️ Sliders Interactivos", layout="centered")
st.header("🎯 Ejemplo personalizado con 4 sliders")

# Slider 1 - Nivel de energía (entero simple)
st.subheader("⚡ ¿Qué tan cargado estás hoy?")
energia = st.slider("Nivel de energía (0 = muerto, 100 = modo Dios)", 0, 100, 50)
st.write("🔋 Nivel actual de energía:", energia)

# Slider 2 - Rango de temperatura deseada
st.subheader("🌡️ Selecciona tu rango de temperatura ideal")
temp_range = st.slider("Temperatura en °C", -10.0, 50.0, (20.0, 25.0))
st.write("🌞 Temperatura ideal: entre", temp_range[0], "°C y", temp_range[1], "°C")

# Slider 3 - Rango de horas para entrenar
st.subheader("🏀 ¿A qué hora entrenas?")
entreno = st.slider("Rango de entrenamiento", value=(time(18, 0), time(20, 0)))
st.write("🕒 Entrenamiento programado de:", entreno[0], "a", entreno[1])

# Slider 4 - Fecha y hora de tu siguiente proyecto
st.subheader("📅 ¿Cuándo arranca tu próximo proyecto importante?")
inicio_proyecto = st.slider(
    "Selecciona fecha y hora",
    value=datetime(2025, 6, 1, 10, 0),
    format="MM/DD/YY - hh:mm"
)
st.write("🚀 El proyecto comienza el:", inicio_proyecto)


