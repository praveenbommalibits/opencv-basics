"""
As part of this, need to understand
1. How to load the image
2. How to load the video
3. How to capture the Video using the webcam

"""

# Import Libraries
import cv2

# Reading the Image from  resources
"""img = cv2.imread("Resources/lena.png")
cv2.imshow("Output", img)
cv2.waitKey(0)"""

# Reading the video file from  resources
"""cap = cv2.VideoCapture("Resources/test_video.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break"""

# Computer /Laptop video capturing
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
