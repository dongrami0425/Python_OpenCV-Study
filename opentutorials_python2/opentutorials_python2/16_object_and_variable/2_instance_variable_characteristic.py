class C(object):
    def __init__(self, v): # 초기화 생성자. # 첫번째 매개변수는 인스턴스자체가 매개변수가 되도록 약속 = self
        self.value = v

    def show(self):
        print(self.value) # 2. 인스턴스의 메소드안에서 인스턴수 변수에접근이 허용
 

c1 = C(10) # 1. 클래스가 인스턴스화 됨.
print(c1.value) 
c1.value = 20 # 3 . 메소드 바깥에서 메소드에(의 변수에) 접근하는 것이 허용.
print(c1.value)
c1.show()
