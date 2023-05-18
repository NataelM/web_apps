import time
import numpy as np
import streamlit as st

st.write("streamlit version = {}".format(st.__version__))
st.latex(r''' e^{i\pi} + 1 = 0 ''')

#barra de progeso
# se coloca la barra de progreso siempre del lado izquierdo 
progress_bar = st.sidebar.progress(0)
# se establece la barra de progeso vacía
status_text = st.sidebar.empty()

last_rows = np.random.randn(1, 1)

#aquí se crea el gráfico de lineas
chart = st.line_chart(last_rows)

for i in range(1,51):
    new_rows = last_rows[-1 , :] + np.random.randn(5,1).cumsum(axis=0)
    #barra de estatus de la barra de progreso
    status_text.text("%i%% Complete" %i)
    #actualización de la barra de progreso
    progress_bar.progress(i)
    #añadiendo los nuevos registros  al gráfico
    chart.add_rows(new_rows)
    #la siguiente linea es para acumular los valores actualizados
    last_rows = new_rows
    
    time.sleep(0.1)

#reseteando la barra d progreso    
progress_bar.empty()
# boton para re ejecutar
st.button('correr')

# para ejecutar esto, desde la consola hacer 
# streamlit run 'nombre.py'