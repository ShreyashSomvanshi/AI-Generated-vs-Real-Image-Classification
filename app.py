import streamlit as st
import tensorflow as tf
import urllib.request
from PIL import Image

st.set_page_config(
    page_title="SynthCheck",
    page_icon="🤖") #layout='wide'

st.title('SynthCheck: A Synthetic Image Identifier ')

#image = Image.open('real vs ai.jpg')
#new_image = image.resize((400, 200))
#st.image(new_image)
# st.image('real vs ai.jpg', width=400)



model = None
#labels = ['real', 'fake']




@st.cache
def load_model():
    global model
    url = 'https://github.com/ShreyashSomvanshi/SynthCheck-A-Synthetic-Image-Identification-using-Deep-Learning/releases/download/testing-model/AIGeneratedModel.h5'
    filename = url.split('/')[-1]
    download_model = urllib.request.urlretrieve(url, fileame)
    model = tf.keras.models.load_model(download_model)

    #model = tf.keras.models.load_model('AIGeneratedModel.h5')


def classify_image(file_path):
    if model is None:
        load_model()
# 
    image = Image.open(file_path) # reading the image
    image = image.resize((32, 32)) # resizing the image to fit the trained model
#     image = image.convert("RGB") # converting the image to RGB
    img = np.asarray(image) # converting it to numpy array
    img = np.expand_dims(img/255, 0)
    predictions = model.predict(img) # predicting the label
    # label = labels[np.argmax(predictions[0])] # extracting the label with maximum probablity
#     probab = float(round(predictions[0][np.argmax(predictions[0])]*100, 2))
    if predictions > 0.5:
        res = 'Predicted class: REAL'
    else:
        res = 'Predicted class: SYNTHETIC'
    
#     result = {
#         'label': label,
#         'probablity': probab
#     }

    return res
    
st.write("Upload an image to check whether it is a fake or real image.")

file_uploaded = st.file_uploader("Choose the Image File", type=["jpg", "png", "jpeg"])
if file_uploaded is not None:
    res = classify_image(file_uploaded)
    c1, buff, c2 = st.columns([2, 0.5, 2])
    c1.image(file_uploaded, use_column_width=True)
    c2.subheader("Classification Result")
    c2.write("The image is classified as **{}**.".format(res.title()))
   # c2.write("The image is classified as **{}**.".format(res['label'].title()))

st.button('Check', use_container_width=True) #use_container_width=True
# st.subheader("Classification Result: ")
