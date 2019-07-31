# < 인스턴스 변수에 외부접근을 제한하는 방법. >
# 외부에서 접근 가능한 변수를 파이썬은 property
# [ __ 란? ]
    #파이썬은 매개변수의 수정과 참조를 할때 메소드를 통하지 않아도 직접 접근이 가능하다 (=파이썬은 기본적으로 속성(instance value)이 인스턴스외부에서 접근이 가능함)
    #이는 파이썬이 객체를 다루는 사용자가 이 객체를 올바르게 사용할 것이라는 믿음을 전제로 하기 때문인데 
    #이런 외부접근을 제한하는 방법으로는 __를 붙여 제한이 가능하다


class C1(object):
    def __init__(self, v):
        self.__value = v # value의 변경을 제한, 접근이 불가능하게 하기위해 __를 붙임.
    
    def setV1(self, v):
        if isinstance(v, int):
            self.__value=v

    def getV1(self):
        return self.__value

    def show(self):
        print(self.__value)

c1 = C1(10)
# print(c1.__value) # 에러. __value에 접근이 불가능.

c1.setV1(20)  # 인스턴스 메소드를 통해서 접근이 가능하다.
print(c1.getV1())
c1.show()
    
   
