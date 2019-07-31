# < 다중 상속 >
# 다중상속은 하나의 클래스가 여러 클래스의 기능을 상속 받는 것을 의미한다. 
# 하나의 자식 객체가 여러 부모 객체의 기능을 상속받는 것.


class C1():
    def c1_m(self):
        print("c1_m")
     
class C2():
    def c2_m(self):
        print("c2_m")
     
class C3(C2, C1): # 다중 상속 클래스. # 
    pass
 
c = C3()
c.c1_m()
c.c2_m()


