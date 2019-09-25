# 참고 URL : https://opencv-python.readthedocs.io/en/latest/doc/27.imageWaterShed/imageWaterShed.html?highlight=distance

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/water_coins.jpg')

# binaray image로 변환
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

#Morphology의 opening, closing을 통해서 노이즈나 Hole제거
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)


# dilate를 통해서 확실한 Backgroud
# 전경과 배경을 구분하기 위해 dilate를 이용하여 경계를 확장
sure_bg = cv2.dilate(opening,kernel,iterations=3)

# 전경은 opening한 결과에 distance transform을 적용하면 중심으로 부터 Skeleton Image를 얻을 수 있음.
# 즉, 중심으로 부터 점점 옅어져 가는 영상.
# 그 결과에 thresh를 이용하여 확실한 FG를 파악
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.5*dist_transform.max(),255,0)
sure_fg = np.uint8(sure_fg)

# Background에서 Foregrond를 제외한 영역을 Unknow영역으로 파악
# 확실하지 않은 영역을 파악. 이것은 이전에 구한 배경에서 전경을 뺀 영역
unknown = cv2.subtract(sure_bg, sure_fg)

# FG에 Labelling작업
# labelling은 서로 이어져 있는 부분에 라벨을 붙여 서로 동일한 객체라는 것을 구분하기 위함
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0

# watershed를 적용하고 경계 영역에 색지정
# watershed함수를 적용 그 결과값이 -1인 영역이 경계값
# 붉은 색을 지정하면 동전의 경계에 붉은 원이 생김
markers = cv2.watershed(img,markers)
print('makers.shape: ',markers.shape,'markers :',markers)
print('붉은색 지정전:',img,'img.shape :', img.shape)
img[markers == -1] = [255,0,0] # matplot으로 이미지를 볼 경우 : (B, G, R) => (R, G, B)순으로 해야 함
print('붉은색 지정후:',img,'img.shape :', img.shape)

images = [gray,thresh,sure_bg,  dist_transform, sure_fg, unknown, markers, img]
titles = ['Gray','Binary','Sure BG','Distance','Sure FG','Unknow','Markers','Result']

for i in range(len(images)):
    plt.subplot(2,4,i+1),plt.imshow(images[i]),plt.title(titles[i]),plt.xticks([]),plt.yticks([])

plt.show()