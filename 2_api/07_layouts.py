import streamlit as st 
import pandas as pd 
import time

#creando el widget de hasta la izquierda
# el side bar siempre va hasta la izquierda
side_bar = st.sidebar

#encabezado del side bar
side_bar.header('Sidebar st.sidebar')
#el caption es como un pequeño trexto sobre intrucciones
side_bar.caption('elements that added in sidebar are pined to left')

##Cargando un csv
df = pd.read_csv('tips.csv')

columns = tuple(df.columns)
st.write(columns)

############ creando una barra seleccionadora
select_column = side_bar.selectbox(
    "Select the column you want to display", # texto de la caja selecionadora
    columns #opciones de la caja seleccionadora
)

#texto de la opcion seleccionada
side_bar.write('You selected the column_name = {}'.format(select_column))

# Dataframe mostrando unicamente la columna seleccionada
st.dataframe(df[[select_column]])


# diseño de tres columnas 
st.header('Columns: st.columns')

#generar las tres columnas
col1, col2, col3 = st.columns(3)

#rellenando la primer columna
with col1:
    st.subheader('columns-1')
    st.image('./media/image.jpg')
#rellenando la segunda columna    
with col2:
    st.subheader('column-2')
    st.dataframe(df)
#rellenando la tercer columna columna
with col3:
    st.subheader('column-3')
    st.dataframe(df[[select_column]])
    
    
# expander caja contenedora que se puede extender
st.header('Expander: st.expander')
#creando el snippet que se expande para mostrar algo más
with st.expander('Some explanation'):
    st.write("""
             Insert a multi-element container that can be expanded/collapsed.

Inserts a container into your app that can be used to hold multiple elements and can be expanded or collapsed by the user. 
When collapsed, all that is visible is the provided label.
    """)
    st.code("""
# you create expander with st.write

import streamlit as st
st.exander('message')
            
            """,language='python')
    
    
# contenedor no desplegable o extendido
st.header('Container st.container')

with st.container():
    st.write('you are inside the container')
    

# Empty: es un elemento que desaperce despues de cierto tiempo
st.header('Empty: st.empty')

placeholder = st.empty()

for i in range(0,11):
    placeholder.write('This message will disappear in {} seconds'.format(10-i))
    time.sleep(1)
    
placeholder.empty() #Aquí se cierra el empty del place holder