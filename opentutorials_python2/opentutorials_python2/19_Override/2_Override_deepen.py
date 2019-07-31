# 계산기 예제. 오버라이드의 활용.

class Cal(object):

    _history = []

    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2

    def add(self):
        result = self.v1+self.v2
        Cal._history.append("add : %d+%d=%d" % (self.v1, self.v2, result))
        return result

    def subtract(self):
        result = self.v1-self.v2
        Cal._history.append("subtract : %d-%d=%d" % (self.v1, self.v2, result))
        return result

    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v

    def getV1(self):
        return self.v1

    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)
    # 부모클래스 info 메소드 : 입력된 변수의 정보를 알려주는 메소드.
    def info(self):
        return "Cal => v1 : %d, v2 : %d" % (self.v1, self.v2)

class CalMultiply(Cal):

    def multiply(self):
        result = self.v1*self.v2
        Cal._history.append("multiply : %d*%d=%d" % (self.v1, self.v2, result))
        return result
    # 오버라이딩 info 메소드1
    def info(self):
        return "CalMultiply => %s" % super().info() # 여기서 super는 Cal 의 info메소드

class CalDivide(CalMultiply):

    def divide(self):
        result = self.v1/self.v2
        Cal._history.append("divide : %d/%d=%d" % (self.v1, self.v2, result))
        return result
    # 오버라이딩 info 메소드2
    def info(self):
        return "CalDivide => %s" % super().info() # 여기서 super는 CalMultiply 의 info메소드
 
c0 = Cal(30, 60)
print(c0.info())

c1 = CalMultiply(10,10)
print(c1.info())

c2 = CalDivide(20,10)
print(c2.info())
