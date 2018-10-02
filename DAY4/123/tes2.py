import numpy as np
import cv2

# xian
img = np.zeros((512,512,3), np.uint8)

# 6px
line = cv2.line(img,(50,50),(11,511),(0,255,0),12)
cv2.imshow('draw_line',line)
cv2.waitKey(0)
