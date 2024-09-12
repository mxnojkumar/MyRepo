import streamlit as st
from PIL import Image

uploaded_image = st.file_uploader("Upload Image") 

with st.expander("Take photo"):
    #open the webcam
    camera_image  = st.camera_input("Camera")

if camera_image:
    #PIL type and function to open and convert
    img = Image.open(camera_image)
    gray_img = img.convert("L")

    #render image in web
    st.image(gray_img)
    
if uploaded_image:
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)