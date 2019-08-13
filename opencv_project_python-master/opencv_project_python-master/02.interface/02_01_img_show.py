# [예제2-1] 이미지 파일을 화면에 표시

import cv2

img_file = "img/girl.jpg" # 표시할 이미지 경로            ---①
img = cv2.imread(img_file)  # 이미지를 읽어서 Numpy배열로 img 변수에 할당 ---②

if img is not None:
  cv2.imshow('IMG', img)   # 읽은 이미지를 화면에 표시, IMG는 창의 제목줄에 나타남      --- ③
  cv2.waitKey()           # 키가 입력될 때 까지 대기      --- ④
  cv2.destroyAllWindows()  # 창 모두 닫기            --- ⑤
else:
    print('No image file.')

'''
[예제2-1]에서 사용한 함수
- img = vc2.imread(file_name [, mode_flag]): 파일로부터 이미지 읽기
- mode_flag=cv2.IMREAD_COLOR : 읽기모드 지정
   cv2.IMREAD_COLOR : 컬러(RGB)스케일로 읽기, default값
   cv2.IMREAD_UNCHANGED : 파일 그대로 읽기
   cv2.IMREAD_GRAYSCALE : 그레이 스케일로 읽기

   - img : 읽은 이미지, NumPy배열타입

- cv2.imshow(title, img) : 이미지를 화면에 표시
    - title : 창 제목, 문자열타입
    - img : (읽은)표시할 이미지, NumPy배열타입

- key = cv2.waitKey([delay]) : 키보드 입력 대기
    - delay = 0 : 키보드 일렵을 대기할 시간(ms), 0은 무한대(기본값으로 입력할 때 까지 기다림)
    - key : 사용자가 입력한 키 값, 정수
        - -1 : 대기시간 동안 키 입력 없음.

'''
    