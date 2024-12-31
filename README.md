# Face-Recognition-based-attendance-system


This project implements a **Face Recognition Attendance System** using OpenCV, dlib, and the face-recognition library. It captures live video from a webcam, detects faces, and matches them against pre-encoded images to mark attendance in a CSV file.

## Features

- Real-time face recognition using webcam.
- Attendance logging with a timestamp and date.
- Text-to-speech feedback for recognized individuals.
- Efficient encoding and face matching with `face_recognition`.
- User-friendly interface for monitoring attendance.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Libraries and Dependencies

Install the required libraries using pip:

```bash
pip install numpy opencv-python face-recognition pyttsx3 geopy
