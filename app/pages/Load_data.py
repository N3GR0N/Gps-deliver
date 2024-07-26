import streamlit as st
import pandas as pd
from defs.def_Load_data import load_and_geocode, save_geocoded_data

def load_data_page():
    st.title("Cargar y Geocodificar Direcciones")

    uploaded_file = st.file_uploader("Subir archivo CSV", type=["csv"])

    if uploaded_file is not None:
        df = load_and_geocode(uploaded_file)
        save_geocoded_data(df, "app/files/geocoded_data.csv")
        st.write("Datos geocodificados:")
        st.write(df)