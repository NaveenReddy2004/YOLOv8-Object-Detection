# YOLOv8-Object-Detection
Project Title: YOLOv8 Real-Time Object Detection
Project Overview
This project implements real-time object detection using YOLOv8, integrated with FastAPI for backend inference and Streamlit for UI interaction.

1. Features
-> Upload images for object detection
-> Real-time detection using webcam
-> FastAPI backend for AI inference
-> Streamlit-based web UI

2. Dataset & Model
-> Dataset: COCO dataset (fetched dynamically)
-> Model: Trained YOLOv8n with custom classes
3. Installation
  - Clone the repository: git clone https://github.com/your-username/YOLOv8-Object-Detection.git
                          cd YOLOv8-Object-Detection
  -Install dependencies: pip install -r requirements.txt
  -Start FastAPI: uvicorn src.api:app --host 0.0.0.0 --port 8000
  -Start Streamlit UI: streamlit run src/app.py
  -Run real-time webcam detection: python src/detect.py
4.Model Training & Optimization
  -Pretrained Model: YOLOv8n (yolov8n.pt)
  -Fine-tuning: Trained on a custom dataset
  -Optimizations: Converted to ONNX for faster inference
