import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

""" The following code is used to adjust filter value
Uncomment to change filter"""
# while True:
#     _, frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     low_thresh = np.array([90,90,2])
#     high_thresh = np.array([180, 255, 255])

#     mask = cv2.inRange(hsv, low_thresh, high_thresh)
#     filtered = cv2.bitwise_and(frame, frame, mask=mask)

#     cv2.imshow("mask", mask)
#     cv2.imshow("filtered", filtered)
#     cv2.imshow("Frame", frame)
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break

low_thresh = np.array([90,90,2])
high_thresh = np.array([180, 255, 255])

start = time.time()

"""get background"""
while int(time.time() - start) < 3:     # wait for seconds
    global background
    _, background = cap.read()
    cv2.imshow("Background", background)
    cv2.waitKey(1)

while True:

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, low_thresh, high_thresh)
    invisible1 = cv2.bitwise_and(background, background , mask = mask)
    mask_inv = 255 - mask
    invisible2 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    invisible = cv2.add(invisible1, invisible2)
    cv2.imshow("Invisibility", invisible)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:                          # escape key
        break


cv2.destroyAllWindows()
cap.release()
