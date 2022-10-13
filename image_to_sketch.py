import cv2

image = cv2.imread("python.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(gray_image)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
inverted_blur = cv2.bitwise_not(blur)
sketch = cv2.divide(gray_image, inverted_blur, scale=250.0)
cv2.imwrite("sketch.png", sketch)