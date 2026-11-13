# 🔫 AI Training Platform

An AI-powered web application built with **FastAPI** and **Ultralytics YOLO** that allows users to upload datasets, train object detection models, and perform real-time weapon detection using a webcam.

## 🚀 Features

* 📹 Live webcam weapon detection
* 🖼️ Image-based object detection
* 🎯 Adjustable confidence threshold
* 🚨 Real-time alarm on weapon detection
* 📦 Dataset upload support
* 🧠 YOLO model training through the web interface
* 📊 Detection results with confidence scores
* 🖍️ Bounding boxes drawn on detected objects
* ⚡ FastAPI backend with REST API
* 🌐 Simple HTML/CSS/JavaScript frontend

---

## 🛠️ Tech Stack

### Backend

* Python 3
* FastAPI
* Uvicorn

### AI & Computer Vision

* Ultralytics YOLO
* PyTorch
* OpenCV

### Frontend

* HTML
* CSS
* JavaScript

---

## 📂 Project Structure

```text
AI-Training-Platform/
│
├── app/
│   ├── routes/
│   ├── services/
│   ├── templates/
│   └── main.py
│
├── models/
│   └── best.pt
│
├── static/
│   └── alarm.mp3
│
├── uploads/
├── datasets/
├── trained_models/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/abdul99088/AI-Training-Platform.git
cd AI-Training-Platform
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the FastAPI server:

```bash
python -m uvicorn app.main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

Webcam Detection:

```
http://127.0.0.1:8000/webcam
```

---

## 📷 Webcam Detection

The webcam module:

* Captures live video
* Sends frames to the FastAPI backend
* Runs YOLO inference
* Draws bounding boxes
* Displays confidence scores
* Plays an alarm when a weapon is detected

---

## 🧠 Model

The project uses a custom-trained **Ultralytics YOLO** model.

Replace the model with your own by placing it in:

```text
models/best.pt
```

---

## 📡 API Endpoints

| Method | Endpoint          | Description                         |
| ------ | ----------------- | ----------------------------------- |
| POST   | `/predict`        | Detect objects in an uploaded image |
| POST   | `/webcam/predict` | Detect objects from webcam frames   |
| POST   | `/upload-dataset` | Upload a training dataset           |
| POST   | `/train`          | Start YOLO model training           |

---

## 📸 Screenshots

Add screenshots here after uploading images to the repository.

Example:

```
screenshots/home.png
screenshots/webcam.png
screenshots/detection.png
```

---

## 🔮 Future Improvements

* Detection history
* Email notifications
* SMS alerts
* Database logging
* Multi-camera support
* User authentication
* Model management dashboard
* Docker deployment

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Abdul Vassay**

GitHub: https://github.com/abdul99088
