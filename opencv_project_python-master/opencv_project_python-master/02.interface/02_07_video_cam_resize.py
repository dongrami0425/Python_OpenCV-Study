# [예제2-7] 카메라 프레임 크기 설정
# 카메라로부터 읽은 영상이 너무 고화질인 경우 픽셀 수를 프레임의 폭과 높이을 제어해서 줄일 수 있다. 

import cv2

cap = cv2.VideoCapture(0)                   # 카메라 0번 장치 연결
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # 프레임 폭 값 구하기
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # 프레임 높이 값 구하기
print("Original width: %d, height:%d" % (width, height) ) 

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)      # 프레임 폭을 320으로 설정 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)     # 프레임 높이를 240으로 설정
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # 재지정한 프레임 폭 값 구하기
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # 재지정한 프레임 폭 값 구하기

print("Resized width: %d, height:%d" % (width, height) )
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('camera', img)
            if cv2.waitKey(1) != -1:
                break
        else:
            print('no frame!')
            break
else:
    print("can't open camera!")
cap.release()
cv2.destroyAllWindows()

'''
아쉽게도 카메라가 아닌 동영상 파일에 프레임 크기를 재지정하는 것은 적용되지 않습니다.
'''