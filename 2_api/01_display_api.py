import pandas as pd
import numpy as np
import streamlit as st 

# display almost anything
# st.write para escribir lo que sea, texto, df, etc
st.write('Hello World')

st.write('Welcome to Streamlit App APIs')

st.write(1234)

df = pd.DataFrame({
    'first_column':[1,2,3,4],
    'second_column': [10,20,30,40]
})

st.write(df)

## display numpy array
st.write(np.array([1,2,3,4]))

## ----------------------------- MAGIC ----------------------------
# sin necesidad de escribir el st.write
# podemos displayear solo poniendo el objeto (como en jupyter )
st.write("Magic commands")

df1 = pd.DataFrame({'col1':[1,2,3,4]})

df1
x = 10
x