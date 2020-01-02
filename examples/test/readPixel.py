

import cv2
import numpy as np

m =  cv2.imread("img_03_class.png")

h,w,bpp = np.shape(m)

for py in range(0,h):
	for px in range(0,w):
		if m[py][px][0] != 0:
			m[py][px][0]=255
			m[py][px][1]=255
			m[py][px][2]=255

cv2.imshow('matrix', m)
cv2.waitKey(0)
cv2.imwrite('img_03_class.png',m)

