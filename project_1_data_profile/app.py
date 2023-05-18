import streamlit as st 
import pandas as pd 
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import sys
import os

#nombre de la pagina e indicamos que la visualización ocupe todo el ancho
st.set_page_config(page_title='Data Profiler',layout='wide')


def get_filesize(file):
    '''
    Funcion que calcula el tamaño en MB
    de un archivo
    '''
    size_bytes = sys.getsizeof(file)
    size_mb = size_bytes / (1024**2)
    return size_mb

def validate_file(file):
    '''
    Esta funcion valida la extension del 
    tipo de archivo que se está cargando
    
    si el archivo es de la extensión validada regresa la extensión
    en otro caso devuelve un false
    '''
    filename = file.name
    name, ext = os.path.splitext(filename) # funcion que regresa el nombre del archivo y la extensión
    if ext in ('.csv','.xlsx'):
        return ext
    else:
        return False
    
################# creacion de la barra latera

## validacion de reporte minimo 
## validación del color del reporte
# sidebar
with st.sidebar:
    uploaded_file = st.file_uploader("Upload .csv, .xlsx files not exceeding 10 MB") #carga del archivo
    if uploaded_file is not None:
        st.write('Modes of Operation')
        minimal = st.checkbox('Do you want minimal report ?')
        display_mode = st.radio('Display mode:',
                                options=('Primary','Dark','Orange'))
        if display_mode == 'Dark':
            dark_mode= True
            orange_mode = False
        elif display_mode == 'Orange':
            dark_mode = False
            orange_mode = True
        else:
            dark_mode = False
            orange_mode = False
        
    
if uploaded_file is not None:
    ext = validate_file(uploaded_file)
    if ext: #si la extensión del archivo es valida
        filesize = get_filesize(uploaded_file)
        if filesize <= 10: #si la extensión del archivo es menor a 10 MB
            if ext == '.csv': # si el archivo es csv que lo lea como csv
                # time being let load csv
                df = pd.read_csv(uploaded_file)
            else: # si el archivo es excel que lo lea como excel
                xl_file = pd.ExcelFile(uploaded_file)
                sheet_tuple = tuple(xl_file.sheet_names)
                sheet_name = st.sidebar.selectbox('Select the sheet',sheet_tuple)
                df = xl_file.parse(sheet_name)
                
                ################## pandas profiling report
            # generate report
            with st.spinner('Generating Report'):
                pr = ProfileReport(df,
                                minimal=minimal,
                                dark_mode=dark_mode,
                                orange_mode=orange_mode
                                )
                
            st_profile_report(pr) #funcion de streamlit para el pandas profiling
        else: # el archivo cargado pesa mas de 10 MB
            
            st.error(f'Maximum allowed filesize is 10 MB. But received {filesize} MB')
            
    else: # no se cargó un csv o un xlsx
        st.error('Kindly upload only .csv or .xlsx file')
        
else: #si no se craga algun archivo
    st.title('Data Profiler')
    st.info('Upload your data in the left sidebar to generate profiling')
    