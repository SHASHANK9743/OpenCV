import cv2
img = cv2.imread("lisa.jpg")
smallLisa = cv2.resize(img, (150, 150))
bigLisa = cv2.resize(img, (600, 600))
cv2.imshow("Lisa my Love", img)
cv2.imshow("Lisa my Small Love", smallLisa)
cv2.imshow("Lisa my Big Love", bigLisa)
cv2.waitKey()