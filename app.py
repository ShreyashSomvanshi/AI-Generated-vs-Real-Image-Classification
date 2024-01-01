import streamlit as st
from PIL import Image

# import util
st.set_page_config(
    page_title="SynthCheck",
    page_icon="🤖") #layout='wide'

st.title('SynthCheck: A Synthetic Image Identifier ')

#image = Image.open('real vs ai.jpg')
#new_image = image.resize((400, 200))
#st.image(new_image)

# st.image('real vs ai.jpg', width=400)
    
st.write("Upload a Picture to check whether it is a fake or real image.")

file_uploaded = st.file_uploader("Choose the Image File", type=["jpg", "png", "jpeg"])
#if file_uploaded is not None:
    #res = util.classify_image(file_uploaded)
#    c1, buff, c2 = st.columns([2, 0.5, 2])
#    c1.image(file_uploaded, use_column_width=True)
#    c2.subheader("Classification Result")
#    c2.write("The image is classified as **{}**.".format(res['label'].title()))

st.button('Check', use_container_width=True) #use_container_width=True
#st.subheader("Classification Result: ")

