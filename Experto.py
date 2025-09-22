# Importar streamlit
import streamlit as st

# Configurar la pagina
st.set_page_config(
    page_title="Guía Little Mac",
    page_icon=":green_heart:", # Usar el comando python -m rich.emoji para ver lista de emojis
    layout="centered",
)


#Crear las multipaginas
pg = st.navigation(["Inicio.py", "Desventaja.py", "Ataques.py", "curiosidades.py", "KO.py", "Conoce.py"])
pg.run()