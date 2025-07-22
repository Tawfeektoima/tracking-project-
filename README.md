# tracking-project-

# Real-Time Object Tracking with OpenCV (CSRT)

A real-time object tracking system that allows the user to manually select an object from the webcam feed and track it using OpenCV's CSRT (Channel and Spatial Reliability Tracking) algorithm.

---
## Features
Real-time webcam capture using `cv2.VideoCapture`, Manual object selection via ROI interface, Object tracking using OpenCV’s **CSRT** tracker, and Visual feedback (green box for "Target", red text for "Lost")

---

## How It Works

1. Capture a single frame from the webcam
2. Prompt the user to select an object (Region of Interest)
3. Initialize the CSRT tracker with the selected ROI
4. Continuously update and display the tracker results on each frame



