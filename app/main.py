import streamlit as st
from pages.Load_data import load_data_page
from defs.def_main import main_page 

st.sidebar.title("Navegación")
page = st.sidebar.selectbox("Selecciona la página", ["Cargar Datos", "Mostrar Camino"])

if page == "Cargar Datos":
    load_data_page()
elif page == "Mostrar Camino":
    main_page()