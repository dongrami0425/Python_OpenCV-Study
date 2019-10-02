import cv2
import numpy as np

img = cv2.imread('img/house.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# SIFT 추출기 생성
sift = cv2.xfeatures2d.SIFT_create()
# 키 포인트 검출과 서술자 계산
keypoints, descriptor = sift.detectAndCompute(gray, None)
print('keypoints:',len(keypoints),'keypoint type',type(keypoints),'descriptor:', descriptor.shape, 'descriptor type:',type(descriptor),descriptor.dtype)
# keypoints:413  keypoint type <class 'list'> descriptor:(413, 128)  descriptor type: <class 'numpy.ndarray'> float32
print(descriptor)

# 키 포인트 그리기
img_draw = cv2.drawKeypoints(img, keypoints, None, \
                flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# 결과 출력
cv2.imshow('SIFT', img_draw)
cv2.waitKey()
cv2.destroyAllWindows()