import cv2
import numpy as np

image = cv2.imread("pika.png")
cv2.imshow("Original Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread("pika.png")

kernel = np.ones((5,5), np.uint8)
eroded = cv2.erode(image, kernel, iterations=1)

cv2.imshow("Eroded Image", eroded)

image = cv2.imread("pika.png")

blurred = cv2.blur(image, (5,5))
cv2.imshow("Blurred Image", blurred)

image = cv2.imread("pika.png")

gaussian = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Guassian Blur", gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()
