import cv2

image = cv2.imread("national-animal-of-Pakistan-markhor.jpg")

rescale = cv2.resize(image, (640, 480))

gray_image = cv2.cvtColor(rescale, cv2.COLOR_BGR2GRAY)

inverted_image = cv2.bitwise_not(gray_image)  # 255 - gray_image

blurred = cv2.bilateralFilter(inverted_image, 21, 75, 75)

inverted_blurred = cv2.bitwise_not(blurred)  # 255 - blurred

pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

cv2.imwrite("output/Original Image.jpg", rescale)

cv2.imwrite("output/Sketch Image.jpg", pencil_sketch)

cv2.waitKey(0)
