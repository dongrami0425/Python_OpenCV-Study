# < 다중 상속의 활용 > - 계산기 예제
# 이번엔 거꾸로 Cal이 CalMultiply와 CalDivide를 다중상속 받도록 해보자.

class CalMultiply():
    def multiply(self):
        return self.v1*self.v2

class CalDivide():
    def divide(self):
        return self.v1/self.v2

class Cal(CalMultiply, CalDivide):
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2

    def add(self):
        return self.v1+self.v2

    def subtract(self):
        return self.v1-self.v2

    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v

    def getV1(self):
        return self.v1

c = Cal(100, 10) # 인스턴스 생성을 Cal에 대해서만 해주어도 CalMultiply, CalDivide의 기능을 모두 사용가능.
print(c.add())
print(c.multiply())
print(c.divide())
