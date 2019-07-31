# 클래스 생성 => 계산기 클래스를 이미 생성했다고 가정해보자.
# 계산기 클래스를 활용한 예제

class Cal(object):
    def __init__(self, v1, v2): #파이썬은 첫번째 매개변수가 해당 인스턴스이어야만 한다.
        self.v1 = v1            #self는 해당 인스턴스를 의미. 하며 변수앞에 써주면 해당 인스턴스에 내장된 변수라는 의미.
        self.v2 = v2
 
    def add(self):
        return self.v1+self.v2
 
    def subtract(self):
        return self.v1-self.v2

# 생성자 : 클래스를 복제한 인스턴스가 생성되고, 생성되는 과정에서 아래 두개의 입력값이 인스턴스에 설정이 된다.
#           생성자란 인스턴스가 만들어 질때 자동으로 실행되도록 약속된 메소드를 생성자라고 한다.
#           클래스에서 def __init__() 로 약속됨.

c1 = Cal(10,10)  #두개의 10은 c1이라는 인스턴스에 내장되는 변수값이다.
print(c1.add())
print(c1.subtract())

c2 = Cal(30,20)
print(c2.add())
print(c2.subtract())
