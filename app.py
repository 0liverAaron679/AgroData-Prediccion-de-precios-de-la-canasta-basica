from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Dashboard Canasta Básica",
    page_icon="🛒",
    layout="wide"
)

# Ruta del CSV
DATA_PATH = Path("canasta_basica_limpia.csv")

@st.cache_data
def cargar_datos():
    df = pd.read_csv(
        DATA_PATH,
        parse_dates=["fecha"],
        dayfirst=True,
        low_memory=False
    )
    return df

# Cargar datos
df = cargar_datos()

# Título
st.title("🛒 Dashboard de Canasta Básica")
st.markdown("Análisis de precios por producto, municipio, estado y marca")

# ==========================
# FILTROS
# ==========================

st.sidebar.header("Filtros")

estado = st.sidebar.multiselect(
    "Estado",
    sorted(df["estado"].unique())
)

producto = st.sidebar.multiselect(
    "Producto",
    sorted(df["producto_normalizado"].unique())
)

marca = st.sidebar.multiselect(
    "Marca",
    sorted(df["marca"].dropna().unique())
)

# Aplicar filtros
df_filtrado = df.copy()

if estado:
    df_filtrado = df_filtrado[
        df_filtrado["estado"].isin(estado)
    ]

if producto:
    df_filtrado = df_filtrado[
        df_filtrado["producto_normalizado"].isin(producto)
    ]

if marca:
    df_filtrado = df_filtrado[
        df_filtrado["marca"].isin(marca)
    ]

# ==========================
# KPIs
# ==========================

st.subheader("Indicadores")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Registros",
    f"{len(df_filtrado):,}"
)

c2.metric(
    "Precio Promedio",
    f"${df_filtrado['precio'].mean():.2f}"
)

st.markdown("[🔗 Ver repositorio en GitHub](https://github.com/0liverAaron679/AgroData-Prediccion-de-precios-de-la-canasta-basica)")