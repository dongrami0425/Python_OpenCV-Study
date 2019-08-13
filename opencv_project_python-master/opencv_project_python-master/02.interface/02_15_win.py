# [예제2-15] 창 관리 API 사용하기
# 한 개 이상의 이미지를 여러 창에 띄우거나 각 창에 키보드와 마우스 이벤트를 처리 하려면 창을 관리하는 기능이 필요합니다.
# - cv2.namedWindow(title [, option]) : 이름을 갖는 창 열기
#       - option : 창 옵션, 'cv2.WINDOW'로 시작
#          - cv2.WINDOW_NORMAL : 임의의 크기, 사용자 창 크기 조정 가능
#          - cv2.WINDOW_AUTOSIZE : 이미지와 같은 크기, 창크기 재조정 불가능.
# - cv2.moveWindow(title, x, y) : 창 위치 이동
# - cv2.resizeWindow(title, width, height) : 창크기 변경
# - cv2.destroyWindow(title) : 창닫기
# - cv2.destroyAllWindows() : 열린 모든 창 닫기
import cv2

file_path = 'img/girl.jpg'
img = cv2.imread(file_path)                            # 이미지를 기본 값으로 읽기
img_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE) # 이미지를 그레이 스케일로 읽기

cv2.namedWindow('origin')                               # origin 이름으로 창 생성 # 옵션을 설정하지 않으면 Default option = cv2.WINDOW_AUTOSIZE
cv2.namedWindow('gray', cv2.WINDOW_NORMAL)              # gray 이름으로 창 생성
cv2.imshow('origin', img)                               # origin 창에 이미지 표시
cv2.imshow('gray', img_gray)                            # gray 창에 이미지 표시

cv2.moveWindow('origin', 0, 0)                          # 창 위치 변경
cv2.moveWindow('gray', 100, 100)                        # 창 위치 변경

cv2.waitKey(0)                                          # 아무키나 누르면
cv2.resizeWindow('origin', 200, 200)                    # 창 크기 변경 (변경 안됨)
cv2.resizeWindow('gray', 100, 100)                      # 창 크기 변경 (변경 됨))

cv2.waitKey(0)                                          # 아무키나 누르면
cv2.destroyWindow("gray")                               # gray 창 닫기

cv2.waitKey(0)                                          # 아무키나 누르면
cv2.destroyAllWindows()                                 # 모든 창 닫기