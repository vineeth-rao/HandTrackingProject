# Hand Tracking Project

This repository contains a Python-based project using OpenCV to track hand movements and implement various interactive applications such as finger counting, virtual painting, and volume control.

---

## Features
- **Finger Counter**: Counts the number of fingers held up in front of the camera.
- **Virtual Painter**: Allows you to draw on the screen using your finger.
- **Volume Control**: Adjusts the system's volume by using finger gestures.

---

## Project Structure

```plaintext
Hand Tracking Project/
│
├── FingerImages/                # Directory containing example images
├── __pycache__/                 # Folder with compiled Python files
├── images/                      # Additional resources and images
├── FingerCounter.py             # Application for finger counting
├── HandTrackingMin.py           # Minimal hand tracking demonstration
├── HandTrackingModule.py        # Core module for hand detection and tracking
├── Header-Files.zip             # Supporting resources in a zip archive
├── VirtualPainter.py            # Application for virtual painting
├── VolumeHandControl.py         # Application for volume control
├── hello.py                     # Initial testing script
├── testcam.py                   # Script for testing webcam functionality
└── README.md                    # Project documentation

## Prerequisites

Ensure you have the following installed:

- **Python 3.6+**
- **OpenCV**: For computer vision functions
- **MediaPipe**: For hand tracking
- **NumPy**: For numerical operations

Install the dependencies with:
```bash
pip install opencv-python mediapipe numpy
