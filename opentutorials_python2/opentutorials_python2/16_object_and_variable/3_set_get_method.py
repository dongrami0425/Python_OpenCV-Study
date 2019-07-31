# < Set/Get method >
# 인스턴스 변수를 읽고 쓰는 방식중에서 권장되는 방법.
# 메소드에 set, get을 붙이는 것은 관습적인 약속.
# 메소드밖(메인코드에서)에서 인스턴스 메소드에 직접적으로 접근한다는 것을 명시하는 방법.

class C(object):
    def __init__(self, v):
        self.value = v
    def show(self):
        print(self.value)

    def getValue(self):
        # 값을 받아오는 메소드.
        return self.value
    def setValue(self, v):
        # 값을 설정하는 메소드.
        self.value = v

c1 = C(10)
print(c1.getValue())
c1.setValue(20)
print(c1.getValue())