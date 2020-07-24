import cv2
import numpy as np


def get_image_types():
    img = cv2.imread("Resources/praveen.jpg")

    # Define the kernal functon
    kernel = np.ones((5, 5), np.uint8)

    # Gray Image
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur Image
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
    # Edge Detector
    imgCanny = cv2.Canny(img, 100, 100)
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=5)
    imgEroded = cv2.erode(imgDilation, kernel, iterations=5)

    cv2.imshow("Gray Image ", imgGray)
    cv2.imshow("Blur Image ", imgBlur)
    cv2.imshow("Canny Image ", imgCanny)
    cv2.imshow("Dilation Image", imgDilation)
    cv2.imshow("Erode Image ", imgEroded)
    cv2.waitKey(0)


def object_resizing():
    img = cv2.imread("Resources/praveen.jpg")
    print(img.shape)

    img_resize = cv2.resize(img, (1000, 500))
    print(img_resize.shape)

    img_cropped = img[0:200, 200:500]
    cv2.imshow("Image ", img)
    cv2.imshow("Image Resize ", img_resize)
    cv2.imshow("Image Cropped ", img_cropped)

    cv2.waitKey(0)

object_resizing()
#get_image_types()
