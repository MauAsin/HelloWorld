import streamlit as st
import pandas as pd
import plotly.express as px

# =================== CONFIGURACIÓN ===================
st.set_page_config(page_title="🚛 Eficiencia en la Última Milla", layout="wide")

# =================== CARGA DE DATOS ===================
@st.cache_data
def load_data():
    return pd.read_csv("Libro1.csv")

df = load_data()

# =================== LIMPIEZA ===================
df['orden_compra_timestamp'] = pd.to_datetime(df['orden_compra_timestamp'], errors='coerce')
df['año'] = df['orden_compra_timestamp'].dt.year
df['mes'] = df['orden_compra_timestamp'].dt.month

# =================== SIDEBAR ===================
st.sidebar.header("🎛️ Filtros")
region = st.sidebar.multiselect("Selecciona región:", df['region'].dropna().unique(), default=df['region'].dropna().unique())
anio = st.sidebar.slider("Selecciona el año:", int(df['año'].min()), int(df['año'].max()), (int(df['año'].min()), int(df['año'].max())))

# =================== FILTRO ===================
df_filtrado = df[(df['region'].isin(region)) & (df['año'] >= anio[0]) & (df['año'] <= anio[1])]

# =================== TÍTULO ===================
st.title("🚛 Eficiencia en la Última Milla: ¿Entregamos Bien o Solo a Tiempo?")

# =================== VISUALIZACIONES ===================
col1, col2 = st.columns(2)

with col1:
    fig1 = px.histogram(df_filtrado, x="desviacion_entrega", nbins=30, title="📉 Distribución de Desviación en Entrega")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.box(df_filtrado, x="region", y="costo_relativo_envio", title="💸 Costo Relativo de Envío por Región")
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    promesas = df_filtrado.groupby("rango_distancia")["desviacion_vs_promesa"].mean().reset_index()
    fig3 = px.bar(promesas, x="rango_distancia", y="desviacion_vs_promesa", title="📦 Desviación vs Promesa por Rango de Distancia")
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    mapa_df = df_filtrado.dropna(subset=['lat_origen', 'lon_origen'])
    fig_mapa = px.scatter_mapbox(mapa_df,
                                 lat="lat_origen",
                                 lon="lon_origen",
                                 hover_name="estado_del_cliente",
                                 zoom=3,
                                 height=500,
                                 title="🗺️ Puntos de Origen de Entregas")
    fig_mapa.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig_mapa, use_container_width=True)


