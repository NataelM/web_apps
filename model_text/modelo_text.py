import streamlit as st
import pandas as pd
import string
#from sklearn.externals import joblib
import joblib
import pickle

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

punctuation = set(string.punctuation)
def tokenize(sentence):
    tokens = []
    for token in sentence.split():
        new_token = []
        for character in token:
            if character not in punctuation:
                new_token.append(character.lower())
        if new_token:
            tokens.append("".join(new_token))
    return tokens

#with open('./niv_vectorizer', 'rb') as vect:
vectorizer = joblib.load('./niv_vectorizer')
#with open('./niv_class_label', 'rb') as sup:
#with open('maq_sup_vect.sav', 'rb') as clssier:
#    svm = pickle.load(clssier)    
#svm = pickle.load(open('maq_sup_vect.sav', 'rb'))

svm = pickle.load(open('maq_sup_vect.pkl', 'rb'))

st.write(type(svm))


st.header('HOMOLOGAR CATEGORIAS (PRUEBA)')

with st.form('myform'):
 
    st.subheader('Prueba de clasificación')
 
    c1, c2, c3 = st.columns(3)
    niv_1 = c1.text_input('nivel_1')
    niv_2 = c2.text_input('nivel_2')
    niv_3 = c3.text_input('nivel_3')

    submitted = st.form_submit_button('categorizar')
    if submitted:
        lista_niveles = [niv_1 + niv_2 + niv_3]

        pred = svm.predict(vectorizer.transform(lista_niveles))
        st.write(f'El ticket habla sobre {pred}')