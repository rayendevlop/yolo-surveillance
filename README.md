# yolo-surveillance
AI Surveillance System with YOLOv8
A real-time AI surveillance system using YOLOv8 to detect people, trigger alerts, and automatically save detection images.
This project uses Ultralytics YOLOv8n (nano version) for fast, lightweight performance on CPU.
🚀 Features
✔ Real-time person detection
✔ Bounding boxes + confidence percentage
✔ Saves every detection with a timestamp
✔ Plays alert sound when a person is detected
✔ Lightweight YOLOv8 (fast even on laptop CPUs)
✔ Works with any webcam
📂 Project Structure
yolo-surveillance/
│── main.py
│── yolov8n.pt
│── detections/
│── alert.mp3
│── README.md
📦 Installation
1. Clone the project
git clone https://github.com/rayendevlop/yolo-surveillance
cd yolo-surveillance
2. Install dependencies
pip install ultralytics opencv-python
▶️ Run the Program
python3 main.py
Press q to quit.
🧠 How It Works
The script loads YOLOv8n
For each camera frame:
Runs object detection
Looks for class 0 = person
Draws bounding box
If a person is detected:
Saves snapshot → detections/
Plays an alert sound (alert.mp3)
📸 Example Output
Saved file:
detections/detection_1735564938.jpg
🛠 Requirements
Python 3.8+
Webcam
YOLOv8 model weights (auto-downloaded by Ultralytics)
🧑‍💻 Author
Rayen Gharbi
AI & Computer Vision Developer
📍 Tunisia
