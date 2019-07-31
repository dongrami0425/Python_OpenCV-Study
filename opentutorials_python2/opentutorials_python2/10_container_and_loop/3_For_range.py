# for 변수 in range() 
# 컨테이너에서 range를 사용하여 for문 사용하기

#i=[0,1,2,3,4]
#for item in i:
#    print(item)

for item in range(0,5): # for문을 위한 리스트를 작성하지않고 range함수를 이용해 for문을 작동시킬수 있음.
                        # range(A,B) => A부터 B-1까지 반복.  
                        # range는 range(시작숫자, 종료숫자, step)의 형태로 리스트 슬라이싱과 유사합니다.
                        # range의 결과는 시작숫자부터 종료숫자 바로 앞 숫자까지 컬렉션을 만듭니다. 
    print(item)

print('*'*30)

for item2 in range(5,51,5):
    print(item2)