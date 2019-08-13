# [예제2-17] 마우스 이벤트
# 마우스에서 입력을 받으려면 이벤트를 처리할 함수를 미리 선언해 놓고 cv2.MouseCallback() 함수에 이벤트 처리 함수를 전달합니다.
# - cv2.MouseCallback(win_name, onMouse [, param]) : onMouse 함수를 등록
#       - win_name : 이벤트를 등록할 창 이름
#       - onMouse : 이벤트 처리를 위해 미리 선언해 놓은 콜백 함수. 함수의 이름은 사용자가 자유롭게 지정가능.
#       - param : 필요에 따라 onMouse 함수에 전달할 인자.

# - MouseCallback(event, x, y, flags, param) : 콜백함수 선언부. # 콜백함수 내부에서 사용하지 않더라도 5개의 인자는 콜백함수는 선언부에 무조건 기재해야 한다.
#       - event: 마우스 이벤트 종류, cv2.EVENT_ 로 시작하는 상수(12가지, 각 상수는 0~11 로 되어있다. 종류는 책을 참조 p.53) 
#       - x, y : 마우스 좌표
#       - flags : 마우스 동작과 함께 일어난 상태, cv2.EVENT_FLAGS_ 로 시작하는 상수(6가지, 1,2,4,8,16,32를 가짐. 종류는 책 참조 p.53)
#                 flags 상수는 2진수 비트자릿수에 맞는 값을 가진다.
#                 만약 전달인자 flag 값이  25와 같은 값이라면 25= 1 + 8 + 16이므로 1,8,16에 맞는(flags 상수에 해당하는) 여러 상태를 나타내는 값을 조합한 값이다.           
#                 따라서  flags 상수(상수명)와 전달인자 flags값을 &, | 연산을 써서 각각을 알아내고 따로따로 비교해야한다.
#       => flags를 활용하는 예제는 [예제2-18]에서 진행.
              

import cv2

title = 'mouse event'                   # 창 제목
img = cv2.imread('img/blank_500.jpg')   # 백색 이미지 읽기
cv2.imshow(title, img)                  # 백색 이미지 표시

def onMouse(event, x, y, flags, param): # 아무스 콜백 함수 구현 ---①                                         
    print(event, flags, x, y, )                # 파라미터 출력
    if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 버튼 누름인 경우 ---②
        cv2.circle(img, (x,y), 30, (0,0,0), -1) # 지름 30 크기의 검은색 원을 해당 좌표에 그림
        cv2.imshow(title, img)          # 그려진 이미지를 다시 표시 ---③

cv2.setMouseCallback(title, onMouse)    # 마우스 콜백 함수를 GUI 윈도우에 등록 ---④


while True:
    if cv2.waitKey(0) & 0xFF == 27:     # esc로 종료
        break
cv2.destroyAllWindows()