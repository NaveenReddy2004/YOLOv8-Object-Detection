# YOLOv8-Object-Detection
📌 Project Title: YOLOv8 Real-Time Object Detection
📌 Project Overview
This project implements real-time object detection using YOLOv8, integrated with FastAPI for backend inference and Streamlit for UI interaction.

📌 Features
✅ Upload images for object detection
✅ Real-time detection using webcam
✅ FastAPI backend for AI inference
✅ Streamlit-based web UI

📌 Dataset & Model
Dataset: COCO dataset (fetched dynamically)
Model: Trained YOLOv8n with custom classes
📌 Installation
1️⃣ Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/YOLOv8-Object-Detection.git
cd YOLOv8-Object-Detection
2️⃣ Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Start FastAPI:

bash
Copy
Edit
uvicorn src.api:app --host 0.0.0.0 --port 8000
4️⃣ Start Streamlit UI:

bash
Copy
Edit
streamlit run src/app.py
5️⃣ Run real-time webcam detection:

bash
Copy
Edit
python src/detect.py
📌 Model Training & Optimization
Pretrained Model: YOLOv8n (yolov8n.pt)
Fine-tuning: Trained on a custom dataset
Optimizations: Converted to ONNX for faster inference
