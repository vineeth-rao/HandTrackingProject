# Hand Tracking Project

This repository contains a Python-based project using OpenCV to track hand movements and implement various interactive applications such as finger counting, virtual painting, and volume control.

---

## Features
- **Finger Counter**: Counts the number of fingers held up in front of the camera.
- **Virtual Painter**: Allows you to draw on the screen using your finger.
- **Volume Control**: Adjusts the system's volume by using finger gestures.

---

## Project Structure

Hand Tracking Project/ │ ├── FingerImages/ # Directory with example images ├── pycache/ # Compiled Python files ├── images/ # Additional resources and images ├── FingerCounter.py # Finger counting application ├── HandTrackingMin.py # Minimal hand tracking example ├── HandTrackingModule.py # Core hand tracking module ├── Header-Files.zip # Zip file with supporting resources ├── VirtualPainter.py # Virtual painting application ├── VolumeHandControl.py # Volume control application ├── hello.py # Initial test script ├── testcam.py # Camera testing script └── README.md # Project documentation
---

## Prerequisites

Ensure you have the following installed:

- **Python 3.6+**
- **OpenCV**: For computer vision functions
- **MediaPipe**: For hand tracking
- **NumPy**: For numerical operations

Install the dependencies with:
```bash
pip install opencv-python mediapipe numpy
