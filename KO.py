#Linea de importación de Streamlit junto a linea que muestra el titulo de la pagina y una imagen

import streamlit as st

st.title("KO")

st.image("Ko.png")
#linea de division
st.divider()
#linea de escritura
st.write("""El K.O es el ataque más fuerte de little Mac, se va cargando poco a poco conforme Litte Mac va recibiendo o haciendo daño (siendo más efectivo recibir daño),
cada ataque de Little Mac posee un valor que muestra la cantidad de barra que carga, aunque en realidad poco importa, el K.O es capaz de quitar stocks realmente temprano, teniendo un porcentaje de muerte
que depende del peso y otras caracteristicas del enemigo.
En enemigos livianos el porcentaje es al 20%.
En personajes pesado entre 30% y 40%.
Y en el caso de Shulk con su arte de Shield puede sobrevivir hasta el 90% con buena DI.
El K.O ignora counters y escudos, ademas de ser invecible al comienzo de su recorrido, aunque todas estas propiedades desaparecen en el aire, volviendose muy inutil a parte de usarse para recuperarse.
Si Little Mac llega a sufrir mucho daño podra llegar a perder el K.O y tendra que volverlo a cargar.

Consejos: Usa el K.O en el suelo y sin miedo, aunque puede ser castigable
""")
    