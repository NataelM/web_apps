import streamlit as st 
import time

## barras de progreso
st.header('st.progress')
st.caption('Display a progress bar')

def progress_bar():  
    for pct_complete in range(1,121,20):
        time.sleep(0.5)
        pct_complete = min(pct_complete,100)
        # el numero de ingesta es la cantidad de progreso que lleva del [1-100]
        my_bar.progress(pct_complete)
    
## spinner
## poner mensaje de espera hasta que se termine de ejecuatar algo
with st.spinner("Something is processing .."):
    my_bar = st.progress(0) #esto es lo que se está ejecutando
    progress_bar()
    
################### mensajes de info exito o error ####################   
# info color azul
st.subheader('st.info')
st.info('This is infomation message')

# success color verde
st.subheader('st.success')
st.success('This is success message')

#warning color amarillo
st.subheader('st.warning')
st.warning('This is warning')

# error color rojo
st.subheader('st.error')
st.error('this is error')

time.sleep(2)
#globitos
st.balloons()