import streamlit as st
import requests
import cv2
import numpy as np
from PIL import Image

st.title("AI Object Detection Interface")
st.write("Upload an image to detect objects.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Detect Objects"):
        # Send image to FastAPI
        response = requests.post("http://127.0.0.1:8000/detect/", files={"file": uploaded_file.getvalue()})

        if response.status_code == 200:
            results = response.json()
            st.write("Detected Objects:")
            for obj in results["detected_objects"]:
                st.write(f"**{obj['label']}** - Confidence: {obj['confidence']}")
        else:
            st.error("Error in detection!")