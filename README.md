# Project Report: Computer Vision Applications - January 2025
# Duration: 
December 10, 2024 - January 10, 2025
# Overview:
This report summarizes a series of computer vision projects developed using Python and libraries such as OpenCV, Mediapipe, NumPy, and PyAutoGUI. The core of this work involved creating custom modules to streamline hand and pose detection, which then served as the foundation for building interactive and practical applications. These projects demonstrate a range of capabilities, including real-time interaction with computer systems.
Key Modules Developed:
Hand Detection Module:
Purpose: To create a reusable component for detecting and tracking hands in video streams.
Function:
Utilizes Mediapipe to detect hands within a video frame.
Identifies key landmarks on the hand, such as fingertips and joints.
Provides information about finger positions (extended or not), enabling gesture recognition.
Technologies: Python, Mediapipe, OpenCV
Pose Estimation Module:
Purpose: To develop a streamlined method for detecting and tracking human poses in video.
Function:
Employs Mediapipe to detect human poses within a video frame.
Identifies key body landmarks, such as shoulders, elbows, and wrists.
Calculates angles between joints, enabling analysis of body posture and movement.
Technologies: Python, Mediapipe, OpenCV, NumPy
Overall Approach:
The initial focus was on developing the Hand Detection and Pose Estimation modules. These modules encapsulated the complex Mediapipe functionality into easy-to-use components. OpenCV was then used for video processing and display, NumPy for numerical calculations (like angle determination), and PyAutoGUI enabled the creation of interactive applications that could control the computer system. With these foundational modules in place, the subsequent application projects were developed.
Project Summaries:
AI Trainer: Real-Time Exercise Analysis
Task: To analyze exercise form (specifically bicep curls) in real-time and provide feedback to the user.
How it Works:
A video feed is analyzed to detect the user's pose using the custom pose estimation module.
The angle of the arm is calculated to determine the curl's progress.
A visual progress bar and a rep counter are displayed to give immediate feedback.
Outcome: A system that can assist users in maintaining proper form during exercise.
Finger Counting: Simple Gesture Recognition
Task: To accurately count the number of fingers a user is holding up.
How it Works:
The hand is detected in the video feed using the custom hand detection module.
The position of the fingertips is analyzed to determine if each finger is extended.
The number of extended fingers is counted and displayed on the screen.
Outcome: A basic gesture recognition application with potential uses in accessibility and simple human-computer interaction.
Virtual Painter: Hand-Controlled Digital Art
Task: To create a virtual painting experience controlled by hand movements.
How it Works:
The hand is tracked using the custom hand detection module.
The user can select colors and an eraser from a virtual palette displayed at the top of the screen, using finger gestures.
The movement of the index finger acts as a brush, drawing on a virtual canvas.
Outcome: A fun and intuitive way to create digital art using hand gestures.
Virtual Mouse: Contactless Computer Control
Task: To control the computer's mouse cursor and clicks using hand movements.
How it Works:
The hand is tracked using the custom hand detection module.
Hand movements are translated into cursor movements on the screen.
A pinching gesture (bringing two fingers close together) simulates a mouse click.
Outcome: Hands-free control of a computer, with potential applications in accessibility and sterile environments.
Volume Control: Gesture-Based Audio Adjustment
Task: To adjust the system's volume using hand gestures.
How it Works:
The hand is tracked using the custom hand detection module.
The distance between the thumb and index finger is measured.
This distance is mapped to the system's volume level, allowing the user to increase or decrease the volume by spreading or closing their fingers.
Outcome: A convenient and intuitive way to control audio volume without physical controls.
Overall Conclusion:
These projects demonstrate the power of modular design in computer vision applications. By first developing reusable hand and pose detection modules, it was possible to create a variety of interactive and practical applications efficiently. This approach highlights the importance of building a strong foundation for future explorations in human-computer interaction and real-time analysis. The use of Mediapipe, OpenCV, and custom-built modules enabled the creation of robust and efficient systems for hand and pose tracking, paving the way for future explorations in human-computer interaction and real-time analysis
