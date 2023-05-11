# Motion Mouse
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)<br/>
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
<br/><sup><sub>AI Virtual Mouse 🖱️</sub></sup>

The Motion Mouse is a virtual mouse that allows you to control your computer using hand gestures. This project uses computer vision and machine learning techniques to detect your hand gestures and simulate mouse movements and clicks. With the Motion Mouse, you can control your computer without touching a physical mouse, which can be particularly useful in situations where a physical mouse is not available or comfortable to use, such as when giving presentations, playing games, or simply when you want to give your wrist a break.
<br/>

![Main-Image](https://github.com/Lahari03/MotionMouse/assets/86518939/290fe315-2761-49f9-8c46-a2e89c166363)
---

## How It Works

The Motion Mouse uses the following technologies:

- Python 3.7 or higher
- OpenCV: an open-source computer vision library that provides a set of tools and algorithms for real-time image processing and analysis.
- MediaPipe: a cross-platform framework for building multimodal machine learning pipelines that can process and analyze audio, video, and other sensor data.
- PyAutoGUI: a Python module for automating keyboard and mouse movements, which allows the Motion Mouse to simulate mouse clicks and movements on your computer.
---

## How to Run

1. Install the required libraries: `pip install -r requirements.txt`
2. Run the main file: `python motion_mouse.py`
3. Hold your hand up in front of the camera and use the specified hand gestures to control the mouse.
---

## Features

| Feature | Description |
|---------|-------------|
| Hand Detection | Detects hand landmarks in real-time using Mediapipe |
| Mouse Movement | Moves the mouse cursor based on the position of the detected hand |
| Left Click | Simulates a left mouse click when the thumb and index finger are close together |
| Right Click | Simulates a right mouse click when the index and middle finger are close together |
<br/>

![Hand-Landmarks](https://github.com/Lahari03/MotionMouse/assets/86518939/89d5fa37-0144-4013-b2c9-8b678cffd079)
---

## Future Improvements

| Improvement | Description |
|-------------|-------------|
| Multi-hand support | Add the ability to detect and control multiple hands simultaneously |
| Gesture customization | Allow users to define their own hand gestures for controlling the mouse |
| Keyboard shortcuts | Add support for keyboard shortcuts using hand gestures |
| GUI | Create a graphical user interface for the application |
| Hand tracking improvement | Improve the hand detection algorithm to better handle occlusions and complex hand poses |

Feel free to contribute to this project by submitting pull requests or creating issues on the GitHub repository!
