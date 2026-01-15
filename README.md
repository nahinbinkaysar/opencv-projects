# Computer Vision Projects

A collection of real-time computer vision applications built with OpenCV, MediaPipe, and YOLO.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Latest-orange.svg)
![YOLO](https://img.shields.io/badge/YOLO-v11-red.svg)

---

## 🎯 Projects

### 1. Face Detection
Real-time face detection using OpenCV's Haar Cascade classifier.

**Features:**
- Webcam-based real-time detection
- Bounding box visualization around detected faces
- Lightweight and fast inference

**Demo:**

<p align="center" width="100%">
<video src="https://github.com/nahinbinkaysar/opencv-projects/releases/download/demo/face-detection.mov" width="80%" controls></video>
</p>

---

### 2. Hand Detection & Landmark Tracking
Real-time hand detection and skeletal landmark tracking using MediaPipe.

**Features:**
- Detects up to 2 hands simultaneously
- 21-point hand landmark detection
- Full skeletal rig visualization (bones connecting joints)
- Fingertip highlighting

**Demo:**

<p align="center" width="100%">
<video src="https://github.com/nahinbinkaysar/opencv-projects/releases/download/demo/hand-detection.mov" width="80%" controls></video>
</p>



---

### 3. Vehicle Detection & Counting
Automated vehicle detection and counting using YOLOv11 with custom tracking logic.

**Features:**
- YOLOv11-based object detection
- Persistent object tracking across frames
- Region-of-interest (ROI) based counting
- Lane-wise vehicle counting (inner/outer lane classification)
- Annotated video output with real-time count overlay

**Demo:**

| Original Video | Annotated Output |
|----------------|------------------|
| <video src="https://github.com/nahinbinkaysar/opencv-projects/releases/download/demo/video.mp4" width="360" controls></video> | <video src="https://github.com/nahinbinkaysar/opencv-projects/releases/download/demo/annotated_video.mp4" width="360" controls></video> |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **OpenCV** | Image processing, video I/O, visualization |
| **MediaPipe** | Hand landmark detection |
| **YOLOv11** | Object detection for vehicles |
| **NumPy** | Numerical operations |
| **Python** | Core language |

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install opencv-python mediapipe ultralytics numpy tqdm
```

### Running the Projects

**Face Detection:**
```bash
python face_detection.py
```

**Hand Detection:**
```bash
python hand_detection.py
```
> Note: The hand landmarker model will be automatically downloaded on first run.

**Vehicle Counting:**
Open `vehicle_detection_counting.ipynb` in Jupyter Notebook and run the cells.

---

## 📁 Project Structure

```
.
├── face_detection.py              # Haar Cascade face detection
├── hand_detection.py              # MediaPipe hand landmark detection
├── vehicle_detection_counting.ipynb   # YOLO-based vehicle counting
├── demos/
│   ├── face_demo.mp4
│   ├── hand_demo.mp4
│   ├── vehicle_original.mp4
│   └── vehicle_annotated.mp4
└── README.md
```

---

## 📊 Results

| Project | Model/Method | FPS (approx) |
|---------|--------------|--------------|
| Face Detection | Haar Cascade | 30+ |
| Hand Detection | MediaPipe | 25-30 |
| Vehicle Counting | YOLOv11x | 15-20 (GPU) |

---

## 👤 Author

**Nahin Bin Kaysar**  
- 🌐 [Portfolio](https://nahinbinkaysar.github.io/)
- 💻 [GitHub](https://github.com/nahinbinkaysar)
- 📧 nahinbinkaysar@gmail.com

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
