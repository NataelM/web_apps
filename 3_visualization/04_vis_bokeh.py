from matplotlib.pyplot import legend
from numpy import source
import streamlit as st 
import pandas as pd 
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

x = [1,2,3,4,5]
y = [6,7,2,4,5]

p = figure(title='Simple Line Chart',
           x_axis_label = 'x',
           y_axis_label = 'y')

#p.line(x,y,line_width=2) #grafico de lineas
p.circle(x,y,size=10) #grafico de scatter
st.bokeh_chart(p) #sentencia especial ara plots de bokeh

# 1. Scatter plot between total_bill and tip
# 2. Scatter plot between total_bill and tip color by options 
#   (sex, smoker, day, time)

data = pd.read_csv('tips.csv')

st.subheader('1. Scatter plot between total_bill and tip')

p = figure(title='Scatter plot between total_bill vs tips')
p.circle('total_bill',y='tip',source=data,size=12) #scatter plot

st.bokeh_chart(p) #sentencia especial ara plots de bokeh

## question -2
##### visualización coloreando los puntos segun las diferentes categorias de  la data 
st.subheader("""
2. Scatter plot between total_bill and tip color by options 
(sex, smoker, day, time)
             """)

p = figure(title='Scatter plot and coloring by categories')
select = st.selectbox('select the categories',
                      ('sex', 'smoker', 'day', 'time'))
color_palette = ['blue','red','green','#D35400','black']
unique_cats = data[select].unique()
index_cmap = factor_cmap(select,palette=color_palette[:len(unique_cats)],
                         factors=sorted(unique_cats))

p.circle('total_bill','tip',source=data,
         fill_color=index_cmap,size=12,legend=select)
st.bokeh_chart(p)#sentencia especial ara plots de bokeh
