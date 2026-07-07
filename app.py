import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

# ============================
# Load Trained Model
# ============================

model = tf.keras.models.load_model("handwritten_character_recognition.keras")

# ============================
# Streamlit Page
# ============================

st.set_page_config(
    page_title="Handwritten Character Recognition",
    page_icon="✍️",
    layout="centered"
)

st.title("✍️ Handwritten Character Recognition")
st.write("Upload a handwritten digit image (28×28 or any size).")

# ============================
# Upload Image
# ============================

uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("L")

    st.image(image, caption="Uploaded Image", width=250)

    image = np.array(image)

    image = cv2.resize(image, (28, 28))

    image = image.astype("float32") / 255.0

    image = image.reshape(1, 28, 28, 1)

    prediction = model.predict(image)

    predicted_class = np.argmax(prediction)

    confidence = np.max(prediction) * 100

    st.success(f"Predicted Character: {predicted_class}")

    st.info(f"Confidence: {confidence:.2f}%")