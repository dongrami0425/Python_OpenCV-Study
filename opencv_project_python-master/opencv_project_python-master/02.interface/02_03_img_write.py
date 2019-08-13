# [예제2-3] 컬러이미지를 그레이 스케일로 저장

import cv2

img_file = 'img/girl.jpg'
save_file = 'img/girl_gray.jpg'

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(img_file, img)
cv2.imwrite(save_file, img) #파일로 저장, 포맷은 확장에 따름
cv2.waitKey()
cv2.destroyAllWindows()

'''
- cv2.imwrite(file_path, img) : 이미지를 파일에 저장
    - file_path : 저장할 파일 경로 이름, 문자열타입
    - img : 저장할 영상, NumPy 배열 타입

'''
