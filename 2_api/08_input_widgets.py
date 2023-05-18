import streamlit as st 
import pandas as pd 
import numpy as np
import os 


# load the data
data = pd.read_csv('tips.csv')

def display_data_random(df):
    sample = df.sample(5)
    return sample
    


###################################### button widget
st.subheader('Displaying Random 5 Rows')
st.caption('click on the button below to display the row randomly')
button = st.button('Display random 5 rows') # asignación y texto del botón
if button: #click es un true 
    sample = display_data_random(data)
    st.dataframe(sample)
    
#######################################3# botón checkbox
st.markdown('---')
st.subheader('st.checkbox')
agree = st.checkbox('I agree to terms and conditions') # return boolean value, texto del boton
st.write('checkbox status =',agree)

########################################### mutiple checkbox
with st.container():
    #mensaje de info del checkbox multiple
    st.info('What technologies you know')
    
    # Lista de opciones del checkbox
    
    python = st.checkbox('Python')
    datascience = st.checkbox('Data Science')
    ai_ml = st.checkbox('AI/ML')
    android = st.checkbox('Android')
    react = st.checkbox('React JS')
    java = st.checkbox('Core Java')
    javascript = st.checkbox('Java Script')
    #botón de enviar
    tech_button = st.button('Submit') # botón de enviar
    if tech_button:
        tech_dict = {
            'Python':python,
            'Data Science':datascience,
            'AI/ML':ai_ml,
            'Android':android,
            'React JS':react,
            'Core Java':java,
            'Java Script':javascript,
        }
        st.json(tech_dict)
        
######################################## radio button: una opcion de diferentes posibles
st.markdown('---')
st.subheader('st.radio')

radio_button = st.radio("what is your favorite color ?", #texto
                        ('White','Black','Pink','Red','Blue','Green') #iterable de opciones
                        )

st.write('Your favorite color is',radio_button)

############################ selectbox se despliega  una caja con las opciones posibles a elegir
st.markdown('---')
st.subheader('st.selectbox')

select_box = st.selectbox('What skill you want to learn most', # texto
                          ('Java','Python','C','C++','JavaScript','HTML','Others')) #opciones
st.write('You selected =',select_box)


############################ multi select
st.markdown('---')
st.subheader('st.multiselect')

options = st.multiselect('What kind of movies you like', #texto
               ['Comedy','Action','Sci-fi','Drama','Romance'] #diferentes opciones de selección
               ) #regresa una lista
st.write('you selected',options)

################################# slider: Barra deslizadora
st.markdown('---')
st.subheader('st.slider')
loan = st.slider(
    'What is loan amout you are looking for ?',
    0,100000,1000,1000 #min, max, default value and step
)
st.write('Loan amount =',loan)

############################################ text input
st.markdown('---')
st.subheader('st.text_input , st.number_input, st.date_input')

with st.container():
    name = st.text_input('Please enter your name') #insertar texto
    age = st.number_input('How old are you',min_value=0,max_value=150,value=25,step=1) #insertar un numero
    decribe = st.text_area('Decription',height=150) #area de texto libre
    dob = st.date_input('Select date of birth')#seleccionar una fecha
    
    submit_button = st.button('Submit Button')
    
    if submit_button: #si se presiona enviar
        info = {
            "Name": name,
            'Age': age,
            'Date of Birth': dob,
            'About Yourself': decribe
        }
        st.json(info) #mostrar un diccionario

###################################### fileuploader
st.markdown('---')
st.subheader('st.file_uploader')

uploaded_file = st.file_uploader('Choose a file') # cargar el archivo
save_button = st.button('save file') #crear boton de guardar
if save_button: #si se guarda el archivo
    if uploaded_file is not None: #si el archivo no es vacío
        with open(os.path.join("./save_folder",uploaded_file.name),mode='wb') as f: #guardar el archivo
            f.write(uploaded_file.getbuffer()) #escribir el archivo
            
        st.success('File uploaded sucessfully') #boton de exito
        
    else:
        st.warning('Please select the file you want to upload') #boton de warningg