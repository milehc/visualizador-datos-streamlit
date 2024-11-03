import streamlit as st
import pandas as pd

st.title('Visualizador de datos Streamlit')

uploaded_file = st.file_uploader('Sube un archivo csv', type=['csv'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

st.table(df)