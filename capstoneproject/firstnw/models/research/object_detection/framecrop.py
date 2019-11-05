import os
from PIL import Image


# -----------------------------------------------------------------------------------------------------------
# 현재 위치 불러와서 이미지 파일 경로 저장
cwd = os.getcwd()
file = cwd + '/image2.jpg'
print('현재 폴더 위치:', cwd)

img = Image.open(file)

# 높이 너비 저장
# height, width = img.shape[0:2]

full_width, full_height = img.size
x_min, x_max, y_min, y_max = 0.0, full_width, 0.0, full_height

# object_width, object_height = object_size
obeject_y_min, obeject_x_min, obeject_y_max, obeject_x_max = \
125.64113295078278, 340.59024143218994, 332.0577321052551, 582.3780236244202


object_width = float(obeject_x_max - obeject_x_min)
object_height = float(obeject_y_max - obeject_y_min)

print("전체 사이즈: (%d, %d)" % (full_width, full_height))

origin_pix_ratio = (object_height * object_width) / (full_width * full_height)
print("원본 이미지와 피사체의 비율 :", origin_pix_ratio)

# print("원하는 피사체의 (x, y) 중심좌표를 입력하라:  ex) 40 200")
# x_coordinate, y_coordinate = input().split()
# #강아지 사진 전체 사진 크기: 738 x 415,  강아지의 중심좌표: (412,245)


# x_coordinate = int(x_coordinate)
# y_coordinate = int(y_coordinate)

x_coordinate = float(479.5)
y_coordinate = float(229.0)
print("피사체 중심좌표: (%f, %f)" % (x_coordinate, y_coordinate))

tar_point = [float(x_coordinate), float(y_coordinate)]

# full_size = [width, height]



def D3_rectangle43_frame(width, height, x, y, z, k):
    object_width, object_height = z, k
    tar_point = [x, y]
    bar_1 = 0.0
    bar_2 = 0.0

    for i in range(70000):
        if object_width > object_height:
            bar_1 = bar_1 + 0.2
            bar_2 = bar_2 + 0.15

        else:
            bar_1 = bar_1 + 0.15
            bar_2 = bar_2 + 0.2

        if tar_point[0] < round(width / 2) and tar_point[1] <= round(height / 2):

            frame_xmin = tar_point[0] - (1 * bar_1)
            frame_xmax = tar_point[0] + (2 * bar_1)
            frame_ymin = tar_point[1] - (1 * bar_2)
            frame_ymax = tar_point[1] + (2 * bar_2)

            frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]







        elif tar_point[0] > round(width / 2) and tar_point[1] <= round(height / 2):

            frame_xmin = tar_point[0] - (2 * bar_1)
            frame_xmax = tar_point[0] + (1 * bar_1)
            frame_ymin = tar_point[1] - (1 * bar_2)
            frame_ymax = tar_point[1] + (2 * bar_2)

            frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]





        elif tar_point[0] <= round(width / 2) and tar_point[1] > round(height / 2):

            frame_xmin = tar_point[0] - (1 * bar_1)
            frame_xmax = tar_point[0] + (2 * bar_1)
            frame_ymin = tar_point[1] - (2 * bar_2)
            frame_ymax = tar_point[1] + (1 * bar_2)

            frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]





        elif tar_point[0] > round(width / 2) and tar_point[1] > round(height / 2):

            frame_xmin = tar_point[0] - (2 * bar_1)
            frame_xmax = tar_point[0] + (1 * bar_2)
            frame_ymin = tar_point[1] - (2 * bar_1)
            frame_ymax = tar_point[1] + (1 * bar_2)

            frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

        pix_ratio = (object_height * object_width) / ((frame_xmax - frame_xmin) * (frame_ymax - frame_ymin))
        if pix_ratio <= 0.82 and pix_ratio > 0.8:
            area = (frame_xmin, frame_ymin, frame_xmax, frame_ymax)
            print('4:3 직사각형 3분할 프레임: 비율 0.82')
            print(area)
            cropped_image = img.crop(area)
            # output = cropped_image.resize((640, 640))
            cropped_image.save('resultimage/D3_rectangle43_frame_082.jpg')
            continue
        if pix_ratio <= 0.56 and pix_ratio > 0.54:
            area = (frame_xmin, frame_ymin, frame_xmax, frame_ymax)
            print('4:3 직사각형 3분할 프레임: 비율 0.56')
            print(area)
            cropped_image = img.crop(area)
            # output = cropped_image.resize((640, 640))
            cropped_image.save('resultimage/D3_rectangle43_frame_056.jpg')
            continue
        if pix_ratio <= 0.1:
            area = (frame_xmin, frame_ymin, frame_xmax, frame_ymax)
            print('4:3 직사각형 3분할 프레임: 비율 0.1')
            print(area)
            cropped_image = img.crop(area)
            # output = cropped_image.resize((640, 640))
            cropped_image.save('resultimage/D3_rectangle43_frame_01.jpg')
            break

def D3_rectangle169_frame(width, height, x, y, z, k):
    object_width, object_height = z, k
    tar_point = [x, y]
    bar_1, bar_2 = 0.0, 0.0
    for i in range(70000):
        if width > height:
            bar_1 = bar_1 + 0.2
            bar_2 = bar_2 + 0.1125

        else:
            bar_1 = bar_1 + 0.1125
            bar_2 = bar_2 + 0.2

        if tar_point[0] < round(width / 2) and tar_point[1] <= round(height / 2):

            frame_xmin = tar_point[0] - (1 * bar_1)
            frame_xmax = tar_point[0] + (2 * bar_1)
            frame_ymin = tar_point[1] - (1 * bar_2)
            frame_ymax = tar_point[1] + (2 * bar_2)

            frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]





        elif tar_point[0] > round(width / 2) and tar_point[1] <= round(height / 2):

            frame_xmin = tar_point[0] - (2 * bar_1)
            frame_xmax = tar_point[0] + (1 * bar_1)
            frame_ymin = tar_point[1] - (1 * bar_2)
            frame_ymax = tar_point[1] + (2 * bar_2)

            frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]





        elif tar_point[0] <= round(width / 2) and tar_point[1] > round(height / 2):

            frame_xmin = tar_point[0] - (1 * bar_1)
            frame_xmax = tar_point[0] + (2 * bar_1)
            frame_ymin = tar_point[1] - (2 * bar_2)
            frame_ymax = tar_point[1] + (1 * bar_2)

            frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]





        elif tar_point[0] > round(width / 2) and tar_point[1] > round(height / 2):

            frame_xmin = tar_point[0] - (2 * bar_1)
            frame_xmax = tar_point[0] + (1 * bar_1)
            frame_ymin = tar_point[1] - (2 * bar_2)
            frame_ymax = tar_point[1] + (1 * bar_2)

            frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

        pix_ratio = (object_height * object_width) / ((frame_xmax - frame_xmin) * (frame_ymax - frame_ymin))
        if pix_ratio <= 0.82 and pix_ratio > 0.8:
            area = (frame_xmin, frame_ymin, frame_xmax, frame_ymax)
            print('16:9 직사각형 3분할 프레임: 비율 0.82')
            print(area)
            cropped_image = img.crop(area)
            # output = cropped_image.resize((640, 640))
            cropped_image.save('resultimage/D3_rectangle169_frame_082.jpg')
            continue
        if pix_ratio <= 0.56 and pix_ratio > 0.54:
            area = (frame_xmin, frame_ymin, frame_xmax, frame_ymax)
            print('16:9 직사각형 3분할 프레임: 비율 0.56')
            print(area)
            cropped_image = img.crop(area)
            # output = cropped_image.resize((640, 640))
            cropped_image.save('resultimage/D3_rectangle169_frame_056.jpg')
            continue
        if pix_ratio <= 0.15:
            area = (frame_xmin, frame_ymin, frame_xmax, frame_ymax)
            print('16:9 직사각형 3분할 프레임: 비율 0.1')
            print(area)
            cropped_image = img.crop(area)
            # output = cropped_image.resize((640, 640))
            cropped_image.save('resultimage/D3_rectangle169_frame_01.jpg')
            break

def center_rectangle43_frame(width, height, x, y, z, k):
    object_width, object_height = z, k
    tar_point = [x, y]
    bar_1 = 0.0
    bar_2 = 0.0

    for i in range(70000):
        if width > height:
            bar_1 = bar_1 + 0.2
            bar_2 = bar_2 + 0.15

        else:
            bar_1 = bar_1 + 0.15
            bar_2 = bar_2 + 0.2

        frame_xmin = tar_point[0] - (1 * bar_1)
        frame_xmax = tar_point[0] + (1 * bar_1)
        frame_ymin = tar_point[1] - (1 * bar_2)
        frame_ymax = tar_point[1] + (1 * bar_2)

        frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

        pix_ratio = (object_height * object_width) / ((frame_xmax - frame_xmin) * (frame_ymax - frame_ymin))
        if pix_ratio == 0.82:
            area = (frame_xmin, frame_ymin, frame_xmax, frame_ymax)
            print('4:3 직사각형 center 프레임: 비율 0.82')
            print(area)
            cropped_image = img.crop(area)
            # output = cropped_image.resize((640, 640))
            cropped_image.save('resultimage/cent_rectangle43_frame.jpg')
            continue
        if pix_ratio == 0.56:
            area = (frame_xmin, frame_ymin, frame_xmax, frame_ymax)
            print('4:3 직사각형 center 프레임: 비율 0.56')
            print(area)
            cropped_image = img.crop(area)
            # output = cropped_image.resize((640, 640))
            cropped_image.save('resultimage/cent_rectangle43_frame.jpg')
            continue
        if pix_ratio == 0.1:
            area = (frame_xmin, frame_ymin, frame_xmax, frame_ymax)
            print('4:3 직사각형 center 프레임: 비율 0.1')
            print(area)
            cropped_image = img.crop(area)
            # output = cropped_image.resize((640, 640))
            cropped_image.save('resultimage/cent_rectangle43_frame.jpg')
            break

def center_rectangle169_frame(width, height, x, y, z, k):
    object_width, object_height = z, k
    tar_point = [x, y]
    bar_1, bar_2 = 0.0, 0.0

    for i in range(70000):
        if width > height:
            bar_1 = bar_1 + 0.2
            bar_2 = bar_2 + 0.1125

        else:
            bar_1 = bar_1 + 0.2
            bar_2 = bar_2 + 0.1125

        frame_xmin = tar_point[0] - (1 * bar_1)
        frame_xmax = tar_point[0] + (1 * bar_1)
        frame_ymin = tar_point[1] - (1 * bar_2)
        frame_ymax = tar_point[1] + (1 * bar_2)

        frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

        pix_ratio = (object_height * object_width) / ((frame_xmax - frame_xmin) * (frame_ymax - frame_ymin))
        if pix_ratio == 0.82:
            area = (frame_xmin, frame_ymin, frame_xmax, frame_ymax)
            print('16:9 직사각형 center 프레임: 비율 0.82')
            print(area)
            cropped_image = img.crop(area)
            # output = cropped_image.resize((640, 640))
            cropped_image.save('resultimage/cent_rectangle169_frame.jpg')
            continue
        if pix_ratio == 0.56:
            area = (frame_xmin, frame_ymin, frame_xmax, frame_ymax)
            print('16:9 직사각형 center 프레임: 비율 0.56')
            print(area)
            cropped_image = img.crop(area)
            # output = cropped_image.resize((640, 640))
            cropped_image.save('resultimage/cent_rectangle169_frame.jpg')
            continue
        if pix_ratio == 0.1:
            area = (frame_xmin, frame_ymin, frame_xmax, frame_ymax)
            print('16:9 직사각형 center 프레임: 비율 0.1')
            print(area)
            cropped_image = img.crop(area)
            # output = cropped_image.resize((640, 640))
            cropped_image.save('resultimage/cent_rectangle169_frame.jpg')
            break




def oversize_btobject_Divison3_frame(width, height, x, y, z, k, a, b, c, d):
    x_min, x_max, y_min, y_max = a, b, c, d
    object_width, object_height = z, k
    tar_point = [x, y]
    bar_1, bar_2 = 0.0, 0.0
    if width > height : #원본사진 가로형----------------------------------------------------------------
        if object_height > object_width:  # 피사체 : 세로 직사각형
            print('원본사진이 가로형입니다')
            print('피사체가 세로형입니다')
            for i in range(70000):
                bar_1 = bar_1 + 0.1

                if tar_point[0] < round(width / 2):  # 세로 중심축 왼쪽

                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (2 * bar_1)
                    frame_ymin = y_min
                    if (0.9 * y_max) <= obeject_y_max <= y_max :
                        frame_ymax = tar_point[1] + (0.5 * object_height)
                    else :
                        frame_ymax = tar_point[1] + (0.55 + object_height)


                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                elif tar_point[0] > round(width / 2): #세로 중심축 오른쪽
                    frame_xmin = tar_point[0] - (2 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)
                    frame_ymin = y_min
                    if (0.9 * y_max) <= obeject_y_max <= y_max :
                        frame_ymax = tar_point[1] + (0.5 * object_height)
                    else :
                        frame_ymax = tar_point[1] + (0.55 * object_height)

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                if frame[0] <= 0 or frame[1] >= width:
                    break

        elif object_height < object_width:  # 피사체 : 가로 직사각형
            print('원본사진이 가로형입니다')
            print('피사체가 가로형입니다')
            for i in range(70000):
                bar_1 = bar_1 + 0.1

                if tar_point[0] < (width / 2):  # 세로 중심축 왼쪽

                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (2 * bar_1)
                    frame_ymin = y_min


                    if (0.90 * y_max) <= obeject_y_max <= y_max :
                        frame_ymax = tar_point[1] + (0.5 * object_height)
                    else :
                        frame_ymax = tar_point[1] + (0.55 * object_height)

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                elif tar_point[0] > (width / 2): #세로 중심축 오른쪽
                    frame_xmin = tar_point[0] - (2 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)
                    frame_ymin = y_min


                    if (0.90 * y_max) <= obeject_y_max <= y_max :
                        frame_ymax = tar_point[1] + (0.5 * object_height)
                    else :
                        frame_ymax = tar_point[1] + (0.55 * object_height)

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                if frame[0] <= 0 or frame[1] >= width:
                    break


    elif height > width : #원본사진이 세로형--------------------------------------------------------------
        if object_height > object_width:  # 피사체 : 세로 직사각형
            print('원본사진이 세로형입니다')
            print('피사체가 세로형입니다')
            for i in range(10000):
                bar_1 = bar_1 + 0.1

                if tar_point[0] < round(width / 2):  # 세로 중심축 왼쪽

                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (2 * bar_1)
                    frame_ymin = y_min

                    if (0.9 * y_max) <= obeject_y_max <= y_max :
                        frame_ymax = tar_point[1] + (0.5 * object_height)
                    else :
                        frame_ymax = tar_point[1] + (0.55 + object_height)

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                elif tar_point[0] > round(width / 2): #세로 중심축 오른쪽
                    frame_xmin = tar_point[0] - (2 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)
                    frame_ymin = y_min

                    if (0.9 * y_max) <= obeject_y_max <= y_max :
                        frame_ymax = tar_point[1] + (0.5 * object_height)
                    else :
                        frame_ymax = tar_point[1] + (0.55 + object_height)

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                if frame[0] <= 0 or frame[1] >= width:
                    break

        elif object_height < object_width:  # 피사체 : 가로 직사각형
            print('원본사진이 세로형입니다')
            print('피사체가 가로형입니다')
            for i in range(10000):
                bar_1 = bar_1 + 0.1

                if tar_point[0] < round(width / 2):  # 세로 중심축 왼쪽

                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)
                    frame_ymin = y_min
                    if (0.9 * y_max) <= obeject_y_max <= y_max:
                        frame_ymax = tar_point[1] + (0.5 * object_height)
                    else:
                        frame_ymax = tar_point[1] + (0.55 + object_height)

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                elif tar_point[0] > round(width / 2): #세로 중심축 오른쪽
                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)
                    frame_ymin = y_min
                    if (0.9 * y_max) <= obeject_y_max <= y_max:
                        frame_ymax = tar_point[1] + (0.5 * object_height)
                    else:
                        frame_ymax = tar_point[1] + (0.55 + object_height)

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                if frame[0] <= 0 or frame[1] >= width:
                    break

    area = (frame_xmin, frame_ymin, frame_xmax, frame_ymax)
    print('예외사진 3분할 프레임')
    print(area)
    cropped_image = img.crop(area)
    # output = cropped_image.resize((640, 640))
    cropped_image.save('resultimage/oversize_btobject_divison3_frame.jpg')

def oversize_btobject_center_frame(width, height, x, y, z, k, a, b, c, d):
    x_min, x_max, y_min, y_max = a, b, c, d
    object_width, object_height = z, k
    tar_point = [x, y]
    bar_1, bar_2 = 0.0, 0.0
    if width > height : #원본사진 가로형----------------------------------------------------------------
        if object_height > object_width:  # 피사체 : 세로 직사각형
            print('원본사진이 가로형입니다')
            print('피사체가 세로형입니다')
            for i in range(70000):
                bar_1 = bar_1 + 0.1

                if tar_point[0] < round(width / 2):  # 세로 중심축 왼쪽

                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)
                    frame_ymin = y_min
                    if (0.90 * y_max) <= obeject_y_max <= y_max :
                        frame_ymax = tar_point[1] + (0.5 * object_height)
                    else :
                        frame_ymax = tar_point[1] + (0.55 + object_height)


                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                elif tar_point[0] > round(width / 2): #세로 중심축 오른쪽
                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)
                    frame_ymin = y_min

                    if (0.90 * y_max) <= obeject_y_max <= y_max :
                        frame_ymax = tar_point[1] + (0.5 * object_height)
                    else :
                        frame_ymax = tar_point[1] + (0.55 * object_height)

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                if frame[0] <= 0 or frame[1] >= width:
                    break

        elif object_height < object_width:  # 피사체 : 가로 직사각형
            print('원본사진이 가로형입니다')
            print('피사체가 가로형입니다')
            for i in range(70000):
                bar_1 = bar_1 + 0.1

                if tar_point[0] < (width / 2):  # 세로 중심축 왼쪽

                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)
                    frame_ymin = y_min

                    if (0.90 * y_max) <= obeject_y_max <= y_max :
                        frame_ymax = tar_point[1] + (0.5 * object_height)
                    else :
                        frame_ymax = tar_point[1] + (0.55 + object_height)


                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                elif tar_point[0] > (width / 2): #세로 중심축 오른쪽
                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)
                    frame_ymin = y_min

                    if (0.90 * y_max) <= obeject_y_max <= y_max :
                        frame_ymax = tar_point[1] + (0.5 * object_height)
                    else :
                        frame_ymax = tar_point[1] + (0.55 * object_height)


                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                if frame[0] <= 0 or frame[1] >= width:
                    break


    elif height > width : #원본사진이 세로형--------------------------------------------------------------
        if object_height > object_width:  # 피사체 : 세로 직사각형
            print('원본사진이 세로형입니다')
            print('피사체가 세로형입니다')
            for i in range(10000):
                bar_1 = bar_1 + 0.1

                if tar_point[0] < round(width / 2):  # 세로 중심축 왼쪽

                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)
                    frame_ymin = y_min

                    if (0.90 * y_max) <= obeject_y_max <= y_max :
                        frame_ymax = tar_point[1] + (0.5 * object_height)
                    else :
                        frame_ymax = tar_point[1] + (0.55 + object_height)

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                elif tar_point[0] > round(width / 2): #세로 중심축 오른쪽
                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)
                    frame_ymin = y_min

                    if (0.90 * y_max) <= obeject_y_max <= y_max :
                        frame_ymax = tar_point[1] + (0.5 * object_height)
                    else :
                        frame_ymax = tar_point[1] + (0.55 + object_height)

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                if frame[0] <= 0 or frame[1] >= width:
                    break

        elif object_height < object_width:  # 피사체 : 가로 직사각형
            print('원본사진이 세로형입니다')
            print('피사체가 가로형입니다')
            for i in range(10000):
                bar_1 = bar_1 + 0.1

                if tar_point[0] < round(width / 2):  # 세로 중심축 왼쪽

                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)
                    frame_ymin = y_min
                    if (0.90 * y_max) <= obeject_y_max <= y_max:
                        frame_ymax = tar_point[1] + (0.5 * object_height)
                    else:
                        frame_ymax = tar_point[1] + (0.55 + object_height)

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                elif tar_point[0] > round(width / 2): #세로 중심축 오른쪽
                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)
                    frame_ymin = y_min
                    if (0.90 * y_max) <= obeject_y_max <= y_max:
                        frame_ymax = tar_point[1] + (0.5 * object_height)
                    else:
                        frame_ymax = tar_point[1] + (0.55 + object_height)

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                if frame[0] <= 0 or frame[1] >= width:
                    break

    area = (frame_xmin, frame_ymin, frame_xmax, frame_ymax)
    print('예외사진 3분할 프레임')
    print(area)
    cropped_image = img.crop(area)
    # output = cropped_image.resize((640, 640))
    cropped_image.save('resultimage/oversize_btobject_center_frame.jpg')

def oversize_topobject_Divison3_frame(width, height, x, y, z, k, a, b, c, d):
    x_min, x_max, y_min, y_max = a, b, c, d
    object_width, object_height = z, k
    tar_point = [x, y]
    bar_1, bar_2 = 0.0, 0.0
    if width > height:  # 원본사진 가로형----------------------------------------------------------------
        if object_height > object_width:  # 피사체 : 세로 직사각형
            print('원본사진이 가로형입니다')
            print('피사체가 세로형입니다')
            for i in range(70000):
                bar_1 = bar_1 + 0.1

                if tar_point[0] < round(width / 2):  # 세로 중심축 왼쪽

                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (2 * bar_1)

                    if (0.1 * y_min) <= obeject_y_min <= y_min :
                        frame_ymin = tar_point[1] - (0.5 * object_height)
                    else:
                        frame_ymin = tar_point[1] - (0.55 * object_height)

                    frame_ymax = y_max
                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                elif tar_point[0] > round(width / 2):  # 세로 중심축 오른쪽
                    frame_xmin = tar_point[0] - (2 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)

                    if (0.1 * y_min) <= obeject_y_min <= y_min:
                        frame_ymin = tar_point[1] - (0.5 * object_height)
                    else:
                        frame_ymin = tar_point[1] - (0.55 * object_height)

                    frame_ymax = y_max

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                if frame[0] <= 0 or frame[1] >= width:
                    break

        elif object_height < object_width:  # 피사체 : 가로 직사각형
            print('원본사진이 가로형입니다')
            print('피사체가 가로형입니다')
            for i in range(70000):
                bar_1 = bar_1 + 0.1

                if tar_point[0] < round(width / 2):  # 세로 중심축 왼쪽

                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (2 * bar_1)

                    if (0.1 * y_min) <= obeject_y_min <= y_min:
                        frame_ymin = tar_point[1] - (0.5 * object_height)
                    else:
                        frame_ymin = tar_point[1] - (0.55 * object_height)

                    frame_ymax = y_max

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                elif tar_point[0] > round(width / 2):  # 세로 중심축 오른쪽
                    frame_xmin = tar_point[0] - (2 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)

                    if (0.1 * y_min) <= obeject_y_min <= y_min:
                        frame_ymin = tar_point[1] - (0.5 * object_height)
                    else:
                        frame_ymin = tar_point[1] - (0.55 * object_height)

                    frame_ymax = y_max

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                if frame[0] <= 0 or frame[1] >= width:
                    break


    elif height > width:  # 원본사진이 세로형--------------------------------------------------------------
        if object_height > object_width:  # 피사체 : 세로 직사각형
            print('원본사진이 세로형입니다')
            print('피사체가 세로형입니다')
            for i in range(10000):
                bar_1 = bar_1 + 0.1

                if tar_point[0] < round(width / 2):  # 세로 중심축 왼쪽

                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (2 * bar_1)

                    if (0.1 * y_min) <= obeject_y_min <= y_min:
                        frame_ymin = tar_point[1] - (0.5 * object_height)
                    else:
                        frame_ymin = tar_point[1] - (0.55 * object_height)

                    frame_ymax = y_max

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                elif tar_point[0] > round(width / 2):  # 세로 중심축 오른쪽
                    frame_xmin = tar_point[0] - (2 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)

                    if (0.1 * y_min) <= obeject_y_min <= y_min:
                        frame_ymin = tar_point[1] - (0.5 * object_height)
                    else:
                        frame_ymin = tar_point[1] - (0.55 * object_height)

                    frame_ymax = y_max

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                if frame[0] <= 0 or frame[1] >= width:
                    break

        elif object_height < object_width:  # 피사체 : 가로 직사각형
            print('원본사진이 세로형입니다')
            print('피사체가 가로형입니다')
            for i in range(10000):
                bar_1 = bar_1 + 0.1

                if tar_point[0] < round(width / 2):  # 세로 중심축 왼쪽

                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)

                    if (0.1 * y_min) <= obeject_y_min <= y_min:
                        frame_ymin = tar_point[1] - (0.5 * object_height)
                    else:
                        frame_ymin = tar_point[1] - (0.55 * object_height)

                    frame_ymax = y_max

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                elif tar_point[0] > round(width / 2):  # 세로 중심축 오른쪽
                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)

                    if (0.1 * y_min) <= obeject_y_min <= y_min:
                        frame_ymin = tar_point[1] - (0.5 * object_height)
                    else:
                        frame_ymin = tar_point[1] - (0.55 * object_height)

                    frame_ymax = y_max

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                if frame[0] <= 0 or frame[1] >= width:
                    break

    area = (frame_xmin, frame_ymin, frame_xmax, frame_ymax)
    print('예외사진 3분할 프레임')
    print(area)
    cropped_image = img.crop(area)
    # output = cropped_image.resize((640, 640))
    cropped_image.save('resultimage/oversize_topobject_divison3_frame.jpg')

def oversize_topobject_center_frame(width, height, x, y, z, k, a, b, c, d):
    x_min, x_max, y_min, y_max = a, b, c, d
    object_width, object_height = z, k
    tar_point = [x, y]
    bar_1, bar_2 = 0.0, 0.0
    if width > height:  # 원본사진 가로형----------------------------------------------------------------
        if object_height > object_width:  # 피사체 : 세로 직사각형
            print('원본사진이 가로형입니다')
            print('피사체가 세로형입니다')
            for i in range(70000):
                bar_1 = bar_1 + 0.1

                if tar_point[0] < round(width / 2):  # 세로 중심축 왼쪽

                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)

                    if (0.1 * y_min) <= obeject_y_min <= y_min:
                        frame_ymin = tar_point[1] - (0.5 * object_height)
                    else:
                        frame_ymin = tar_point[1] - (0.55 * object_height)

                    frame_ymax = y_max
                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                elif tar_point[0] > round(width / 2):  # 세로 중심축 오른쪽
                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)

                    if (0.1 * y_min) <= obeject_y_min <= y_min:
                        frame_ymin = tar_point[1] - (0.5 * object_height)
                    else:
                        frame_ymin = tar_point[1] - (0.55 * object_height)

                    frame_ymax = y_max

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                if frame[0] <= 0 or frame[1] >= width:
                    break

        elif object_height < object_width:  # 피사체 : 가로 직사각형
            print('원본사진이 가로형입니다')
            print('피사체가 가로형입니다')
            for i in range(70000):
                bar_1 = bar_1 + 0.1

                if tar_point[0] < round(width / 2):  # 세로 중심축 왼쪽

                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)

                    if (0.1 * y_min) <= obeject_y_min <= y_min:
                        frame_ymin = tar_point[1] - (0.5 * object_height)
                    else:
                        frame_ymin = tar_point[1] - (0.55 * object_height)

                    frame_ymax = y_max

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                elif tar_point[0] > round(width / 2):  # 세로 중심축 오른쪽
                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)

                    if (0.1 * y_min) <= obeject_y_min <= y_min:
                        frame_ymin = tar_point[1] - (0.5 * object_height)
                    else:
                        frame_ymin = tar_point[1] - (0.55 * object_height)

                    frame_ymax = y_max

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                if frame[0] <= 0 or frame[1] >= width:
                    break


    elif height > width:  # 원본사진이 세로형--------------------------------------------------------------
        if object_height > object_width:  # 피사체 : 세로 직사각형
            print('원본사진이 세로형입니다')
            print('피사체가 세로형입니다')
            for i in range(10000):
                bar_1 = bar_1 + 0.1

                if tar_point[0] < round(width / 2):  # 세로 중심축 왼쪽

                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)

                    if (0.1 * y_min) <= obeject_y_min <= y_min:
                        frame_ymin = tar_point[1] - (0.5 * object_height)
                    else:
                        frame_ymin = tar_point[1] - (0.55 * object_height)

                    frame_ymax = y_max

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                elif tar_point[0] > round(width / 2):  # 세로 중심축 오른쪽
                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)

                    if (0.1 * y_min) <= obeject_y_min <= y_min:
                        frame_ymin = tar_point[1] - (0.5 * object_height)
                    else:
                        frame_ymin = tar_point[1] - (0.55 * object_height)

                    frame_ymax = y_max

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                if frame[0] <= 0 or frame[1] >= width:
                    break

        elif object_height < object_width:  # 피사체 : 가로 직사각형
            print('원본사진이 세로형입니다')
            print('피사체가 가로형입니다')
            for i in range(10000):
                bar_1 = bar_1 + 0.1

                if tar_point[0] < round(width / 2):  # 세로 중심축 왼쪽

                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)

                    if (0.1 * y_min) <= obeject_y_min <= y_min:
                        frame_ymin = tar_point[1] - (0.5 * object_height)
                    else:
                        frame_ymin = tar_point[1] - (0.55 * object_height)

                    frame_ymax = y_max

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                elif tar_point[0] > round(width / 2):  # 세로 중심축 오른쪽
                    frame_xmin = tar_point[0] - (1 * bar_1)
                    frame_xmax = tar_point[0] + (1 * bar_1)

                    if (0.1 * y_min) <= obeject_y_min <= y_min:
                        frame_ymin = tar_point[1] - (0.5 * object_height)
                    else:
                        frame_ymin = tar_point[1] - (0.55 * object_height)

                    frame_ymax = y_max

                    frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

                if frame[0] <= 0 or frame[1] >= width:
                    break

    area = (frame_xmin, frame_ymin, frame_xmax, frame_ymax)
    print('예외사진 3분할 프레임')
    print(area)
    cropped_image = img.crop(area)
    # output = cropped_image.resize((640, 640))
    cropped_image.save('resultimage/oversize_topobject_center_frame.jpg')

# -------------------------------------------------------------------------------------------------------------------run


if object_width >= (0.4 * full_width) or object_height >= (0.4 * full_height): #원본사진에 비해 피사체의 크기가 작은경우
    if tar_point[1] > (y_max / 2) : # 피사체가 아래에있는 경우
        print('피사체가 사진의 아래쪽에 배치되어있습니다.')

        oversize_btobject_Divison3_frame(full_width, full_height, tar_point[0], tar_point[1], \
                                       object_width, object_height, x_min, x_max, y_min, y_max)

        oversize_btobject_center_frame(full_width, full_height, tar_point[0], tar_point[1], \
                                   object_width, object_height, x_min, x_max, y_min, y_max)
        print('입력한 사진에 대한 적절한 크롭을 완료 및 제시하였다. 사용자는 사진을 선택하시오.')

    elif tar_point[1] < (y_max / 2) : #피사체가 위에 있는 경우
        print('피사체가 사진의 위쪽에 배치되어있습니다.')

        oversize_topobject_Divison3_frame(full_width, full_height, tar_point[0], tar_point[1], \
                                         object_width, object_height, x_min, x_max, y_min, y_max)

        oversize_topobject_center_frame(full_width, full_height, tar_point[0], tar_point[1], \
                                       object_width, object_height, x_min, x_max, y_min, y_max)
        print('입력한 사진에 대한 적절한 크롭을 완료 및 제시하였다. 사용자는 사진을 선택하시오.')

else: #원본사진에 비해 피사체의 크기가 작은 경우
    D3_rectangle43_frame(full_width, full_height, tar_point[0], tar_point[1], object_width, object_height)

    D3_rectangle169_frame(full_width, full_height, tar_point[0], tar_point[1], object_width, object_height)

    center_rectangle43_frame(full_width, full_height, tar_point[0], tar_point[1], object_width, object_height)

    center_rectangle169_frame(full_width, full_height, tar_point[0], tar_point[1], object_width, object_height)

    print('입력한 사진에 대한 적절한 크롭을 완료 및 제시하였다. 사용자는 사진을 선택하시오')

#-----------------------------------------------------------------------------------------------------------------------
"""
def D3_square_frame (width, height, x, y, z, k) :
    object_width, object_height = z, k
    tar_point = [x, y]
    bar = 10

    for i in range(738):
        bar = bar + 1

        if tar_point[0] < round(width / 2) and tar_point[1] <= round(height / 2):

            frame_xmin = tar_point[0] - (1 * bar)
            frame_xmax = tar_point[0] + (2 * bar)
            frame_ymin = tar_point[1] - (1 * bar)
            frame_ymax = tar_point[1] + (2 * bar)

            frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]





        elif tar_point[0] > round(width / 2) and tar_point[1] <= round(height / 2):

            frame_xmin = tar_point[0] - (2 * bar)
            frame_xmax = tar_point[0] + (1 * bar)
            frame_ymin = tar_point[1] - (1 * bar)
            frame_ymax = tar_point[1] + (2 * bar)

            frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]





        elif tar_point[0] <= round(width / 2) and tar_point[1] > round(height / 2):

            frame_xmin = tar_point[0] - (1 * bar)
            frame_xmax = tar_point[0] + (2 * bar)
            frame_ymin = tar_point[1] - (2 * bar)
            frame_ymax = tar_point[1] + (1 * bar)

            frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]





        elif tar_point[0] > round(width / 2) and tar_point[1] > round(height / 2):

            frame_xmin = tar_point[0] - (2 * bar)
            frame_xmax = tar_point[0] + (1 * bar)
            frame_ymin = tar_point[1] - (2 * bar)
            frame_ymax = tar_point[1] + (1 * bar)

            frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

        pix_ratio = (object_height * object_width) / ((frame_xmax - frame_xmin) * (frame_ymax - frame_ymin))
        if pix_ratio >= 0.09 and pix_ratio <= 0.13:
            break

    area = (frame_xmin, frame_ymin, frame_xmax, frame_ymax)
    print('640x640 정사각형 3분할 프레임')
    print(area)
    cropped_image = img.crop(area)
    output = cropped_image.resize((640, 640))
    output.save('resultimage/square_frame.jpg')
"""

"""
def center_square_frame (width, height, x, y, z, k) :
    object_width, object_height = z, k
    tar_point = [x, y]
    bar = 10

    for i in range(738) :
        bar = bar + 1

        frame_xmin = tar_point[0] - (1 * bar)
        frame_xmax = tar_point[0] + (1 * bar)
        frame_ymin = tar_point[1] - (1 * bar)
        frame_ymax = tar_point[1] + (1 * bar)

        frame = [frame_xmin, frame_xmax, frame_ymin, frame_ymax]

        pix_ratio = (object_height * object_width) / ((frame_xmax - frame_xmin) * (frame_ymax - frame_ymin))
        if pix_ratio >= 0.09 and pix_ratio <= 0.13:
            break

    area = (frame_xmin, frame_ymin, frame_xmax, frame_ymax)
    print(' 640x640 정사각형 center 프레임')
    print(area)
    cropped_image = img.crop(area)
    output = cropped_image.resize((640, 640))
    output.save('resultimage/center_square_frame.jpg')
"""