import streamlit as st
st.set_page_config(page_title="📈 Línea de gráficos", layout="centered")
import pandas as pd
import numpy as np


st.header("📊 Visualización con `st.line_chart`")

# Chart 1: Simulación de precios de Bitcoin
st.subheader("💰 Simulación de precios de Bitcoin (random walk)")
dias = 100
precio = np.cumsum(np.random.randn(dias) * 500 + 20000)
df_btc = pd.DataFrame({'Día': range(1, dias + 1), 'Precio BTC': precio})
st.line_chart(df_btc.set_index('Día'))

# Chart 2: Tendencia de temperatura diaria
st.subheader("🌡️ Temperatura simulada en Monterrey (°C)")
dias = 30
temp = 30 + np.sin(np.linspace(0, 3 * np.pi, dias)) * 5 + np.random.randn(dias)
df_temp = pd.DataFrame({'Día': range(1, dias + 1), 'Temperatura': temp})
st.line_chart(df_temp.set_index('Día'))

# Chart 3: Visitas a una página web por semana
st.subheader("🌐 Visitas semanales a una página ficticia")
semanas = 12
visitas = np.random.randint(100, 1000, size=semanas)
df_web = pd.DataFrame({'Semana': range(1, semanas + 1), 'Visitas': visitas})
st.line_chart(df_web.set_index('Semana'))
