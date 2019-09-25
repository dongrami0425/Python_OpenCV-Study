import cv2
import numpy as np

img = cv2.imread('./img/sunset.jpg')

x=320; y=150; w=320; h=150        # roi 좌표
roi = img[0:y+h, 0:x+w]         # roi 지정        ---①

print(roi.shape)                # roi shape, (50,50,3)
cv2.rectangle(roi, (0,0), (w-1, h-1), (0,255,0)) # roi 전체에 사각형 그리기 ---②

cv2.rectangle(roi, (0,0), (30, 20), (0,0,255)) # roi 전체에 사각형 그리기 ---②

cv2.imshow("img", img)

key = cv2.waitKey(0)
print(key)
cv2.destroyAllWindows()