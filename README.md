# Face Recognition Project

## Overview
This project is a face recognition application developed as part of the Class 12I Project 2023-24 for Delhi Public School Bangalore East. It includes a web-based camera interface and Python scripts for real-time face and person detection using OpenCV.

## Features
- **Web Camera Interface** (`facerecog.html`): A simple HTML page to start/stop the camera, capture photos, and control camera settings (pan, tilt, zoom if supported).
- **Face Detection** (`face_detection.py`): Real-time face detection with bounding boxes drawn around detected faces in the webcam feed.
- **Person Detection** (`person_detection.py`): Checks for the presence of a person (via face detection) and prints status messages to the console.

## Requirements
- Python 3.13.7 or later
- Webcam (built-in or external)
- Web browser with camera permissions enabled
- Virtual environment (already set up in `.venv/`)

## Dependencies
- `opencv-python` (for face detection scripts)
- Modern web browser (for HTML interface)

## Installation and Setup
1. Ensure you have Python installed.
2. Navigate to the project directory: `cd C:\Users\badri\Downloads\BADRI_PROJECTS\face_recog`
3. Activate the virtual environment: `.\.venv\Scripts\Activate.ps1`
4. Install dependencies (if not already done): `pip install opencv-python`

## Usage
### Running the Python Scripts
1. Activate the virtual environment as above.
2. Run face detection: `python face_detection.py` (press 'a' to exit).
3. Run person detection: `python person_detection.py` (press ESC to exit).

### Running the Web Interface
1. Start a local server: `python -m http.server 8000`
2. Open `http://localhost:8000/facerecog.html` in your browser.
3. Use the buttons to control the camera and capture photos.

## File Structure
- `facerecog.html`: Web page for camera control and photo capture.
- `face_detection.py`: Script for drawing rectangles around detected faces.
- `person_detection.py`: Script for detecting person presence with console output.
- `.venv/`: Virtual environment directory.
- `README.md`: This file.

## Notes
- The HTML interface may require camera permissions in the browser.
- Ensure the Haar cascade file (`haarcascade_frontalface_default.xml`) is available (included with OpenCV).
- For any issues, check console output or browser developer tools.

## Author
Class 12I, Delhi Public School Bangalore East (2023-24)</content>
<parameter name="filePath">c:\Users\badri\Downloads\BADRI_PROJECTS\face_recog\README.md
