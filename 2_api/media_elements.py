import streamlit as st 

# Image
st.header('Display image using st.image')

st.image('./media/image.jpg', caption='Beautiful city', width=500)

# Video
st.header('Display video')

video_file = open('./media/waterfalls.mp4', mode='rb')
video_bytes = video_file.read()

st.video(video_bytes)

# Audio
st.header('Display audio')
audio_file = open('./media/audio.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes)