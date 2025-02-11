# WiDS Project 2024-25: Enabling Gesture Control using Computer Vision

This is my project report for the Winter in Data Science (WiDS) program, conducted by the Analytics Club, IIT Bombay. The project took place from December 10, 2024, to January 25, 2025.
Introduction
In this winter project, I explored how to use hand gestures to control a computer system using MediaPipe's 'Hands' module. The goal was to create cool applications like volume control and mouse control—all powered by hand movements captured through a live video feed.
MediaPipe Hands is a powerful tool developed by Google that can detect 21 key points on a hand using machine learning. If you provide it with an image of a hand, it returns the exact positions of these landmarks in 3D space. This makes it a great choice for gesture-based applications.
Understanding Hand Landmarks
MediaPipe represents a hand using 21 landmark points, each with x, y, and z coordinates:
•	x and y are normalized between 0 and 1, based on the image size.
•	z represents depth, where the wrist is considered the origin. A smaller z value means the point is closer to the camera.
By tracking how these landmarks move, we can map different hand gestures to system commands. To make my code reusable, I created a separate Python module (HandTrackingModule.py) containing all the necessary functions for hand detection and landmark tracking.
Implementing Volume and Mouse Control
1. Volume Control
To control system volume using gestures, I used an external Python library called pycaw. Pycaw is designed for managing audio settings on Windows, allowing us to adjust volume programmatically.
2. Mouse Control
For controlling the mouse using hand movements, I used the Mouse module in Python. This library lets us move the cursor, simulate clicks, and perform various other mouse actions through code.
What I Learned
This project gave me hands-on experience with gesture recognition and its real-world applications. While I focused on simple system controls, similar technology is widely used in:
•	Robotics
•	Virtual and Augmented Reality (VR & AR)
•	Home automation
•	Smart multimedia devices
With this project, I have learned the basics of gesture-based control and look forward to exploring more advanced applications in the future. This is just the beginning—I am excited to build more useful and innovative projects using computer vision!
Vision realized, with more to come. 🚀

