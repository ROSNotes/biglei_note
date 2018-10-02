import cv2

img = cv2.imread('/home/intel/Desktop/image.jpg',0)

cv2.imshow("Dispay",img)

cv2.waitKey(0)

cv2.destroyAllWindows()
