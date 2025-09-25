#Linea de importación de Streamlit junto a linea que muestra el titulo de la pagina y una imagen

import streamlit as st

st.title("Desventaja")

st.image("Prepucio.jpg")
#linea de division
st.divider()

st.write("La parte más compleja e importante de un combate es la desventaja, que como dice su nombre es la situación donde tu estas en desventaja frente a tu rival, en el caso de Little Mac esta situación se presenta cuando se encuentra fuera del escenario, contando con opciones muy limitadas para volver a este las cuales deben ser aprovechas al maximo, cosa que se explicara a continuación")
#linea de division
st.divider()
#linea de titulo
st.title("Salto")
#linea de imagen junto a un subtitulo
st.image("salto.jpg", caption="Little Mac saltando")
#linea de division
st.divider()
#linea de escritura
st.write("Little Mac cuenta con un salto que cuenta con una altura media-alta, esto lo hace poder recorrer una buena distancia mientras se encuentra en el aire (Aunque ojo con el fast fall), esta sera su herramienta más sagrada para recuperarse ya que si te llegan a interrumpir, puedes considerarte muerto. La recomendación que te dare aqui es... No entres en panico, lo que mayoria hace es apenas salen del escenario es gastar su salto, cosa que puede terminar condenandolos, en su lugar utiliza su Air-Dodge, siendo intangible y permitiendote avanzar lo suficiente como para ocupar la siguiente opción.")
#linea de division
st.divider()
#linea de titulo
st.title("Side-B")
#linea de imagen
st.image("invencible.jpg")
#linea de division
st.divider()
#linea de escritura
st.write("Contando con buen daño y un buen recorrido el Side B se vuelve una herramiente realmente crucial al momento de recuperarse, el Side-B puede controlar la distancia que recorre, asi pudiendo hacer mixups que obliguen al oponente a identificar cada situación lo cual da segundos cruciales, eso si, el movimiento cuenta con un aspecto realmente malo y es que cuenta con un frame lag de 28 frames, lo que significa que una vez el ataque termine tendras que esperar 22 frames para poder realizar otra accion como saltar o usar el Up-B cosa que puede hacer que antes de que actues ya estes cayendo mucho más abajo de lo que puede llegar el Up-B. La recomendación en este caso es usar el Side-B tras haber ocupado el salto, asi habiendo ganado una altura decente, o en caso extremos usarlo para recuperarse de manera baja, aunque su mejor uso sera para estar sobre el escenario en el caso de haber sido lanzado de manera vertical.")
#linea de division
st.divider()
#linea de titulo
st.title("Counter")
#linea de imagen
st.image("counter.jpg")
#linea de division
st.divider()
#linea de escritura
st.write("Esta opcion es una mucho más de nicho, el Down-B o counter de Little Mac le permite aguantar un golpe y dar un golpe mucho más fuerte despues, haciendole avanzar y dañando al enemigo en el proceso, buena opción para volver al escenario cuando pienses que el enemigo va ir a golpearte pero no es una que puedas abusar constantemente debido a sus 28 frames de End lag.")
#linea de division
st.divider()
#linea de titulo
st.title("Up-B")
#linea de imagen
st.image("imagen0.png")
#linea de division
st.divider()
#linea de escritura
st.write(
    """ El up-B de Little Mac es su utlima (y peor) opción para recuperarse de su desventaja, tiene un recorrido vertical realmente bajo y en horizontal es simplemente pauperrimo, algo que no muchos saben es que
    en los primeros 3 frames es completamente invencible pero además puede ser dirigida levemente hacia un dirección si tiras del joystick aun es algo realmente inutil, esta opción la ocuparas principalmente cuando
    te vayas a recuperar de forma baja, aunque puedes ser facilmente gympeado.""")
#linea de division
st.divider()
#linea de titulo
st.title("Conclusión")
#linea de escritura
st.write(""" Para finiquitar esta sección dejare entonces el orden de como un buen Little Mac deberia volver al escenario; En el caso de recuperarse medio-alto el orden seria Air-Dodge, salto y Side-B,
para recuperarse bajo el orden seria Air-dodge, salto, Side-B y Up B.
Existen otras opciones de nicho como lo son el down air o usar el K.O pero son tecnicas que si bien puedne ayudar se utilizan en niveles altos y no ofrecen gran recompensa.""")
#Dividir en secciones
st.divider()
#Añadir un video para que el usuario pueda interactuar con el
st.video("https://youtu.be/s5pmkY3Ff7Y?si=75J9DKBFNbol-hzY")


