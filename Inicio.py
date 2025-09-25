#Linea de importación de Streamlit junto a linea que muestra el titulo de la pagina

import streamlit as st
#lineas dedicadas al diseño de la web desde la pestaña
st.set_page_config(
    page_title="Guía Little Mac",
    page_icon=":green_heart:", # Usar el comando python -m rich.emoji para ver lista de emojis
    layout="centered",
)
#linea de titulo
st.title("¡Bienvenido a la mejor guía del mundo!")
#linea de division
st.divider()
#linea de imagen
st.image("R.jpg")
#linea de escritura
st.write("Si estas aqui es porque quieres covertirte en el mejor Little Mac de la historia, en esta guía aprenderas cada pequeño detalles, sus ataques, habilidades especiales, y más, excepto sobre el smash final, eso es pa tontos. ")
#linea de division
st.divider()
#linea de escritura
st.write("""Little Mac es un personajes realmente extremo, muy solido en tierra firme pero con una desventaja realmente terrible al poseer malos aereos y una recuperación mediocre, por lo que cualquier persona que decida usarlo de Main va a tener que enfocarse en mantenerse lo más posible en el escenario,
sera complicado pero con gran recompensa ya que Little Mac es uno de los personajes con mayor potential kill de todos, con ataques capaces a de matar a porcentajes realmente bajos y un buen jugador siempre sera capaz de volverse una amenaza importante.""")
#Dividir la pagina en secciones
st.divider()
#Agregar un audio interactuable para el usuario
st.audio("Mac.mp3")
#Escribir en la pagina
st.write("Algunos sonidos de Little Mac")



