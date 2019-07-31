# Enumerate
# 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 때 사용
# 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환한다.
t = [1, 5, 7, 33, 39, 52]

for enum in enumerate(t):
    print(enum)

'''
(0, 1)
(1, 5)
(2, 7)
(3, 33)
(4, 39)
(5, 52)
'''

# tuple형태 반환을 이용하여 아래처럼 활용할 수 있습니다.

for i, v in enumerate(t):
    print("index : {}, value: {}".format(i,v))

'''
index : 0, value: 1
index : 1, value: 5
index : 2, value: 7
index : 3, value: 33
index : 4, value: 39
index : 5, value: 52
'''