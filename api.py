from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
from ultralytics import YOLO
from io import BytesIO
from PIL import Image

app = FastAPI()

# Load trained YOLO model
model = YOLO(r"C:\Users\navee\Desktop\ML\.ipynb_checkpoints\best.pt")  # Update with your trained model path

@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...)):
    # Read image
    image = Image.open(BytesIO(await file.read()))
    image = np.array(image)

    # Run YOLO detection
    results = model(image)

    detected_objects = []
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            label = result.names[int(box.cls[0])]
            conf = float(box.conf[0])
            detected_objects.append({
                "label": label,
                "confidence": round(conf, 2),
                "bbox": [x1, y1, x2, y2]
            })

    return {"detected_objects": detected_objects}
