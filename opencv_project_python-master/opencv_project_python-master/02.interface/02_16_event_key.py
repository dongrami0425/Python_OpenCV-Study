# [예제2-16] 키 이벤트

import cv2

img_file = "img/girl.jpg" 
img = cv2.imread(img_file) 
title = 'IMG'                   # 창 이름 
x, y = 100, 100                 # 최초 좌표

while True:
    cv2.imshow(title, img)
    cv2.moveWindow(title, x, y)
    key = cv2.waitKey(0) & 0xFF # 키보드 입력을 무한 대기, 8비트 마스크처리 
                                # 0xFF는 하위 8비트가 모두 1로 채워진 숫자이므로 이것과 & 연산을 수행하면 하위 8비트 위의 비트느 모두 0으로 채울 수 있다.


    print(key, chr(key))        # 키보드 입력 값,  문자 값 출력
    if key == ord('h'):         # 'h' 키 이면 좌로 이동
        x -= 10
    elif key == ord('j'):       # 'j' 키 이면 아래로 이동
        y += 10
    elif key == ord('k'):       # 'k' 키 이면 위로 이동
        y -= 10
    elif key == ord('l'):       # 'l' 키 이면 오른쪽으로 이동
        x += 10
    elif key == ord('q') or key == 27: # 'q' 이거나 'esc' 이면 종료
        break
        cv2.destroyAllWindows()
    cv2.moveWindow(title, x, y )   # 새로운 좌표로 창 이동
        