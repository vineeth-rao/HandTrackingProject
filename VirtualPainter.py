import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

folderPath = "images"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))

header = overlayList[0]
print(header.shape)
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = htm.HandDetector(detectionCon=0.85)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        print(lmList)

        x1, y1 = lmList[8][1:]  # tip of index
        x2, y2 = lmList[12][1:]  # tip of middle finger

        

    # Setting The Header Image
    img[0:62, 0:640] = header

    cv2.imshow("Image", img)
    cv2.waitKey(1)
