# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 10:49:29 2021

@author: PC
"""

import cv2
img=cv2.imread('sah.jpg',1)
print(img.shape)
print(img.size)

height, width = img.shape[:2] 

grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imwrite('grayimage.jpg',grayImage)
cv2.imshow(' gray image ',grayImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
