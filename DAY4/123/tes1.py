import numpy as np

import cv2

cap = cv2.VideoCapture(2)

while(True):
	ret, frame = cap.read()
	gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	huidu90=np.rot90(gray)
	cv2.imshow('HUISE',gray)
	cv2.imshow('HUI90',huidu90)
	cv2.imshow('frame',frame)
	if cv2.waitKey(1)& 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
