import cv2
import numpy

print('some string')
print('Close this window for continue')
photo = numpy.zeros((450, 450, 3), dtype='uint8')

photo[:] = 165, 150, 73
photo[100:150, 200:280] = 165, 0, 230

cv2.rectangle(photo, (20, 20), (150, 100), (255, 0, 130), thickness=3)
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (255, 255, 255), thickness=2)

cv2.imshow('Photo', photo)
cv2.waitKey(0)

x = 1

img = cv2.imread('images/img.jpg')
img = cv2.resize(img, (img.shape[1] // x, img.shape[0] // x))
img = cv2.GaussianBlur(img, (5, 3), 4)
img = cv2.Canny(img, 150, 200)

kernel = numpy.ones((5, 5), numpy.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)

cv2.imshow('Result', img)

cv2.waitKey(0)

print("Hello!!!")
print("Thanks for attention")

