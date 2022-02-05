import cv2
import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
import os

# class names
# MODEL_NUMBER = max([int(i) for i in os.listdir("2")])
CLASS_NAMES = ['Tomato_Bacterial_spot', 
               'Tomato_Early_blight', 
               'Tomato_healthy', 
               'Tomato_Late_blight', 
               'Tomato_Leaf_Mold', 
               'Tomato_Septoria_leaf_spot', 
               'Tomato_Spider_mites_Two_spotted_spider_mite', 
               'Tomato__Target_Spot', 
               'Tomato__Tomato_mosaic_virus', 
               'Tomato__Tomato_YellowLeaf__Curl_Virus']

# for i in os.listdir("../Dataset"):
#     CLASS_NAMES.append(i)


# GUI
st.title("TOMATO LEAF DISEASE DETECTION APP")
# st.markdown("<h1 style='text-align: center; color: gray;'><B>PATATO DISEASE CLASSIFICATION</B></h1>", unsafe_allow_html=True)
st.write("*..............................This Project was owned by* Vivek Patidar *all the licence belongs to him................................*")


#model building
# MODEL = tf.keras.models.load_model("../Saved_Models/"+str(MODEL_NUMBER))
# MODEL = tf.keras.models.load_model("2")


img_file_buffer = st.camera_input("Take The Picture Of The Leaf")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    image = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
  
    
    # st.image(image, caption='Uploaded Image.', use_column_width=True)
#     image = np.array(image)
#     image = np.expand_dims(image, 0)
#     predictions = MODEL.predict(image)
#     prediction = np.argmax(predictions)
#     confidence = np.max(predictions)
#     pred = CLASS_NAMES[prediction]
#     st.subheader('Prediction : %s' %(CLASS_NAMES[prediction]))
#     st.subheader('Confidence : %f percentage' %(confidence*100))


