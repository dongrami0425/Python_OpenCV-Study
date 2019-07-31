class Cal(object):
    
    _history = [] # 2. 클래스 변수를 배열로 선언.

    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2

    def add(self):
        result = self.v1+self.v2
        Cal._history.append("add : %d+%d=%d" %(self.v1, self.v2, result)) # 배열을 String으로 저장.
        # 3. 연산이 실행 될때마다 result에 결과를 담고. 
        # 4. _history[] 클래스 변수에 배열 함수 append()로 기록을 해준다.
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

    @classmethod      # 1. 클래스 메소드 선언.
    def history(cls): #    계산 history를 보여주는 메소드.
        for item in Cal._history:
            print(item)

class CalMultiply(Cal):
    def multiply(self):
        result = self.v1*self.v2
        Cal._history.append("multiply : %d*%d=%d" % (self.v1, self.v2, result))
        return result

class CalDivide(CalMultiply):
    def divide(self):
        result = self.v1/self.v2
        Cal._history.append("divide : %d/%d=%d" % (self.v1, self.v2, result))
        return result


c1 = CalMultiply(10,10)
print(c1.add())
print(c1.multiply())

c2 = CalDivide(20,10)
print(c2, c2.add())
print(c2, c2.multiply())
print(c2, c2.divide())
Cal.history()
