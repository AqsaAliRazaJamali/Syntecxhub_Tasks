# Real-Time Hand Gesture Recognition & Media Control

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Computer%20Vision-MediaPipe-success?style=for-the-badge" alt="Computer Vision">
  <img src="https://img.shields.io/badge/Project-Hand%20Gesture%20Recognition-blue?style=for-the-badge" alt="Project">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge" alt="Status">
</p>

<p align="center">
  An intelligent <strong>Computer Vision</strong> application that recognizes hand gestures in real time using a webcam.<br>
  The system maps recognized gestures to media control actions through deep-learning hand-tracking models.
</p>

---

## Project Overview

This project tracks hand landmarks from a live webcam feed using **MediaPipe Hands**. By extracting precise landmark coordinates, computing Euclidean distances, and evaluating relative spatial relationships between joints, the application classifies hand gestures such as:

- ✋ Open Palm
- ✊ Fist
- 👍 Thumbs Up

Each recognized gesture is immediately mapped to a corresponding media control action.

Developed as **Task 3** during my **Artificial Intelligence Internship** at **Syntecxhub**.

---

## Core Features

- **Dynamic Hardware Interfacing**  
  Captures real-time video frames directly from the webcam using OpenCV.

- **High-Fidelity Landmark Tracking**  
  Utilizes **Google MediaPipe Hands** to detect and track **21 three-dimensional hand landmarks** with low latency.

- **Geometric Gesture Classification**  
  Classifies gestures by evaluating:
  - Relative Y-axis landmark positions
  - Euclidean distance thresholds
  - Finger state relationships

- **Gesture-to-Action Mapping**

| Gesture | Action |
|----------|--------|
| ✋ Open Palm | `PLAY MEDIA` |
| ✊ Fist | `PAUSE MEDIA` |
| 👍 Thumbs Up | `VOLUME UP` |

- **Real-Time Heads-Up Display (HUD)**  
  Displays detected gestures and corresponding media actions directly on the live video feed.

---

## Tech Stack & Dependencies

| Library / Tool | Purpose |
|----------------|---------|
| **Python 3** | Core development language |
| **OpenCV (`opencv-python`)** | Webcam capture, image processing, color conversion, frame rendering, and overlays |
| **MediaPipe** | Deep-learning hand landmark detection and tracking |
| **math** | Euclidean distance calculations between landmarks |

---

## Project Structure

```text
Syntecxhub_Tasks/
│
├── Syntecxhub_AStar_Maze/
│
├── Syntecxhub_Sentiment_Analysis/
│
└── Syntecxhub_Hand_Gesture_Recognition/
    ├── gesture_control.py      # Main computer vision application
    ├── requirements.txt        # Project dependencies
    ├── .gitignore              # Git ignore rules
    └── README.md               # Project documentation
```

---

## Installation & Setup

### 1️⃣ Navigate to the Project Directory

```bash
cd Syntecxhub_Tasks/Syntecxhub_Hand_Gesture_Recognition
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python gesture_control.py
```

> **Note:** Press **`q`** at any time to stop the webcam and close the application safely.

---

## Algorithmic Logic Breakdown

### 1. Finger State Detection

To determine whether a finger is **open** or **closed**, the application compares the vertical position of the fingertip with its corresponding MCP (metacarpophalangeal) joint.

Mathematically,

```text
Y_tip < Y_mcp
```

Since image coordinates increase downward, a smaller **Y-coordinate** indicates that the fingertip is positioned higher on the screen.

---

### 2. Euclidean Distance Calculation

To distinguish a **Thumbs Up** gesture from a closed **Fist**, the application computes the Euclidean distance between the thumb tip and the index finger MCP joint.

```text
d = √((x1 - x2)² + (y1 - y2)²)
```

Python implementation:

```python
def get_distance(p1, p2):
    return math.sqrt(
        (p1.x - p2.x) ** 2 +
        (p1.y - p2.y) ** 2
    )
```

If the computed distance exceeds **0.12** while the remaining fingers remain folded, the gesture is classified as a **Thumbs Up**.

---

## 👩‍💻 Author

### **Aqsa Jamali**

**AI Intern @ Syntecxhub**

Passionate about **Artificial Intelligence, Computer Vision, and Machine Learning**.

---

## 📄 License

This project was developed exclusively for **academic learning and internship evaluation purposes** under the **Syntecxhub AI Internship Program**.

---

⭐ If you found this project useful, consider giving it a star!
