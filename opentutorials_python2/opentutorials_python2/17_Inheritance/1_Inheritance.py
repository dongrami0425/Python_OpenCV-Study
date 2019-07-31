# < Inheritance >
# 어떤 객체를 만들었을 때, 그 객체의 기능을 받아 다른 기능을 더하여 새로운 객체를 만들어내는 행위. 
# 자신이나 혹은 타인이 만든 객체에 새로운 기능을 추가하여 새로운 기능의 객체를 만들어 내는 것.
# 상속이란 기능을 받는 것을 말한다.

# <상속의 문법> - 실습

# before inheritance
''' 

class Class1(object):
    def method1(self): 
        return 'm1'

class Class3(object):
    def method1(self): 
        return 'm1'
    def method2(self): 
        return 'm2'
'''

# after inheritance : 위의 코드는 상속을 선언하기 전의 코드이다. 두클래스간에 비슷한 성격을 가지지만 코드의 중복이 발생한다.
#                     이를 막기위해 상속을 사용하여 아래 코드처럼 중복을 제거하였다.

class Class1(object): 
    def method1(self): 
        return 'm1'

class Class3(Class1): # 1. class3가 Class1을 상속받았다는 의미.
    def method2(self): 
        return 'm2'

c1 = Class1()
print(c1, c1.method1())
print('-'*50)

c3=Class3()   
print(c3, c3.method1()) # 2. Class1의 메소드를 받아서 사용이 가능하다.
print(c3, c3.method2()) # 3. 인스턴스변수명을 써주면 어디서 실행되는 것인지 확인이 가능.
#[작동 순서]
# c3.method1()을 호출하면 c3라는 인스턴스의 클래스를 찾는다.
# 이제 그 클래스안에서  method1이 존재하는지 찾는다. 없다면 그의 부모를 찾게된다.
# 이제 부모 클래스에서 method1을 찾고 있으면 리턴해준다.


#[실행결과]
#<__main__.Class1 object at 0x0000021DD2F0F630> m1
#--------------------------------------------------
#<__main__.Class3 object at 0x0000021DD3054438> m1
#<__main__.Class3 object at 0x0000021DD3054438> m2


class Class2(object): # 상속을 받지않은 일반적인 객체.

    def method1(self): 
        return 'm1'

    def method2(self): 
        return 'm2'

print('-'*50)
c2 = Class2()
print(c2, c2.method1())
print(c2, c2.method2())

#[실행 결과]
#<__main__.Class2 object at 0x0000021DD3054518> m1
#<__main__.Class2 object at 0x0000021DD3054518> m2