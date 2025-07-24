import streamlit as st
import os

file_path = "image"
files = os.listdir(file_path)
st.write(files)

image_size = st.number_input(
    "圖片大小", min_value=50, max_value=500, value=300, step=50
)

for image in files:
    st.image(f"{file_path}/{image}", width=image_size)
