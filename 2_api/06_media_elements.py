import streamlit as st 

st.header('Display image using st.image')

st.image('./media/image.jpg',caption='Beautiful City',width=500)

############################cargando y mostrando un video
#lectura del video 
st.header('Display video')
video_file = open('./media/waterfalls.mp4','rb')
video_bytes = video_file.read()

#montandp el video en streamlit
st.video(video_bytes)

###################################cargando y mostrando un audio
# display audio
#lectura del audio
st.header('Display audio')
audio_file = open('./media/audio.mp3','rb')
audio_bytes = audio_file.read()

#montando el audio en streamlit
st.audio(audio_bytes,format='audio/ogg')