# 계산기 예제에 곱하기와 나누기를 추가한다. => 클래스 상속을 이용하여 기존의 계산기 클래스에대한 상속클래스를 만들어
#                                            곱하기와 나누기 기능을 추가.
class Cal(object):
    def __init__(self, v1, v2):
        print('-'*100)
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
       
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v

    def getV1(self):
        return self.v1

    def setV2(self, v):
        if isinstance(v, int):
            self.v2 = v

    def getV2(self):
        return self.v2

    def add(self):
        return self.v1+self.v2

    def subtract(self):
        return self.v1-self.v2



class CalMultiply(Cal): # 1. 현재 CalMultiply에는 생성자가 없다. 따라서 실행시 부모에서 생성자를 찾는다.
    def multiply(self):
        return self.v1*self.v2

class CalDivide(CalMultiply):
    def divide(self):
        return self.v1/self.v2



c1 = CalMultiply(10,10)
print(c1, c1.add()) # 2. 부모가 가지는 메소드를 상속받았기 때문에 사용 가능.
print(c1, c1.multiply())

c2 = CalDivide(20,10)
print(c2, c2.add())
print(c2, c2.multiply())
print(c2, c2.divide())
