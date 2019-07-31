# < 다중 상속의 단점(문제점) >
# 만약 상속받은 독립적인 두 부모 안의 메소드 중에서 이름이 같은 메소드가 있다면? 


class C1():
    def c1_m(self):
        print("c1_m")
    def m(self):
        print("C1 m")
 
class C2():
    def c2_m(self):
        print("c2_m")
    def m(self):
        print("C2 m")
 
class C3(C1, C2): # 다중 상속 클래스. # 2. 같은 이름의 메소드는 상속을 받은 순서대로 우선순위를 갖는다.
    #def m(self):                   # 3. 그러나 C3클래스에서 같은이름의 메소드를 가지면 본인의 메소드를 실행한다.
    #    print("C3 m")
    pass
 
c = C3()
c.c1_m()
c.c2_m()
c.m()               # 1. 만약 m메소드가 C3에 없다면 C1, C2중에 어떤 부모의 m메소드를 사용할까?
print(C3.__mro__)

# 4. 따라서 C3에 m메소드가 없다면 => class C3(C1, C2): => c.m()은 C1의 m메소드가 실행
#                                => class C3(C2, C1): => c.m()은 C2의 m메소드가 실행

#           C3에 m메소드가 있다면 => class C3(C2, C1): => c.m()은 C3의 m메소드가 실행
#                                => class C3(C2, C1): => c.m()은 C3의 m메소드가 실행