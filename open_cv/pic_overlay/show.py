import cv2

img_file = 'data/image_640_480.jpg'
img = cv2.imread(img_file, 1)

cv2.imshow('imshow', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
