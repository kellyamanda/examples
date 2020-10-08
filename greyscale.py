import streamlit as st
from PIL import Image

st.set_option('deprecation.showfileUploaderEncoding', False)
image = st.file_uploader("Select an image!")

col1, col2 = st.beta_columns(2)

original = Image.open(image)
col1.header("Original")
col1.image(original, use_column_width=True)

grayscale = original.convert('LA')
col2.header("Grayscale")
col2.image(grayscale, use_column_width=True)
