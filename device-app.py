import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt

# Load the model
model = load_model('device-classification.keras')

# Define the image_predict function
def image_predict(image):
    # Convert PIL image to a NumPy array
    image = np.array(image)
    test_i = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert to BGR for OpenCV
    test_i = cv2.resize(test_i, (256, 256))
    test_input = test_i.reshape((1, 256, 256, 3))
    
    arr = np.array(model.predict(test_input))
    value = arr[0, 0]
    if value == 0:
        return "Laptop"
    else:
        return "Mobile"

# Streamlit app
st.title("Device Classification App")
st.write("Upload an image to classify the device.")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    st.write("")
    st.write("Classifying...")
    
    # Classify the image
    result = image_predict(image)
    
    # Display the results
    st.write("Prediction: ", result)
