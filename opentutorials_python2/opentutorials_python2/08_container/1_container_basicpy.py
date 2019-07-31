# 컨테이너
# 여러 개의 값을 하나의 공간에 담는 것.
# => 리스트와 튜플이 있다.

# 리스트
name = 'dongmin'
print(name) #dongmin
print(type(name)) # <class 'str'>
print(type(['dongmin', 'leezche', 'graphittie'])) #<class 'list'>
#type(데이터) => 데이터의 형식을 알려주는 함수.
#index : 리스트 데이터 순서에 맞게 할당되는 번호(색인). 0부터 시작.
#element : 데이터 원소(요소)

names = ['dongmin', 'leezche', 'graphittie']
print(names) 
print(names[2]) #graphittie
dongmin = ['programmer', 'seoul', 27, False]
dongmin[1] = 'busan' #리스트의 특정 value를 변경.
print(dongmin) #['programmer', 'busan', 27, False]