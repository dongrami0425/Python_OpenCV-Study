def print_a(): #def 는 함수선언시 사용하는 함수선언자. def 함수_명(매개변수1,매개변수2,....)
    print("aaa") #함수 로직을 써줌.

def add(a,b): 
    result = a + b
    return result
print_a()
print(add(1,3))

# 람다를 이용한 add function
'''
add=lambda a,b: a+b => 한줄로 함수의 설정과 기능까지 완료됨.

result = add(3,4)
print(result)
'''
