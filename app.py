import streamlit as st
import cv2
import torch
import numpy as np
from ultralytics import YOLO
from PIL import Image

# Load trained YOLO model
model = YOLO(r"C:\Users\navee\Desktop\ML\.ipynb_checkpoints\best.pt")  # Update with your model path

# Streamlit UI
st.title("Real-Time Object Detection with YOLOv8")
st.sidebar.header("Settings")
run = st.sidebar.button("Start Webcam")

# Webcam video capture
if run:
    cap = cv2.VideoCapture(0)  # 0 for built-in webcam, change to 1 for external

    # Streamlit video display
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture video")
            break

        # Perform YOLO detection
        results = model(frame)

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = result.names[int(box.cls[0])]
                conf = float(box.conf[0])

                # Draw bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Convert frame to RGB for Streamlit
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame, channels="RGB", use_column_width=True)

    cap.release()
else:
    st.warning("Click 'Start Webcam' to begin object detection.")

