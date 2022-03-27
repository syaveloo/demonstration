import cv2
import numpy as np


def getimg(path):
    img = cv2.imread(path, 0)
    kernel = np.ones((3, 3), np.uint8)

    ret, thresh = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY)
    erosion = cv2.erode(thresh, kernel, iterations=1)

    w, h = 64, 16

    dim = (w, h)

    resized = cv2.resize(erosion, dim, interpolation=cv2.INTER_AREA)
    ret, thresh = cv2.threshold(resized, 230, 255, cv2.THRESH_BINARY)

    return img, thresh


orig, img = getimg(path=r"6.jpeg")


def get_letters(img):
    x = -12
    y = 0
    h = 16
    w = 12
    for i in range(1, 6):
        x += w
        yield img[y:y+h, x:x+w]


letters = get_letters(img=img)
for x in range(5):
    cv2.imshow("hey", next(letters))
    cv2.waitKey(0)
