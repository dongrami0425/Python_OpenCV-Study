# [예제2-5] 카메라(웹캠) 프레임 읽기

import cv2

cap = cv2.VideoCapture(0)               # 0번 카메라 장치 연결 ---①
if cap.isOpened():                      # 캡쳐 객체 연결 확인
    while True:
        ret, img = cap.read()           # 다음 프레임 읽기
        if ret:
            cv2.imshow('camera', img)   # 다음 프레임 이미지 표시            
            if cv2.waitKey(1) != -1:    # 1ms 동안 키 입력 대기 ---② : 0을 입력하면 무한대로 대기하기 때문에 1ms를 넣어준 것.
                                        # : => 지정한 대기 시간 동안 키 입력이 없으면 -1을 반환한다. 따라서 반환된 값이 -1이 아니면 아무 키나 입력 되었다는 뜻.
                break                   # 아무 키라도 입력이 있으면 중지 
        else:
            print('no frame')
            break
else:
    print("can't open camera.")
cap.release()                           # 자원 반납
cv2.destroyAllWindows()