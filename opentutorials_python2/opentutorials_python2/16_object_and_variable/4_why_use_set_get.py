# < Set/Get 메소드를 사용하는 이유 >
# 예를 들어 이전 계산기 소스코드의 메인에서
# c1=Cal()
# c1.v1 = 'one'
# c1.v2 = 30
# print(c1.add())
# 로 직접데이터를 set하면 데이터 타입이 맞지 않기 때문에 메소드 실행시 에러가 발생한다.

# 우리는 이러한 문제 때문에 데이터 타입을 제한적으로 허용해야하고 잘못된 결과가 나오는 것을 예방해야한다.
# 

class Cal1(object):

    def __init__(self, v1, v2):
        # 
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2

    def add(self):
        return self.v1+self.v2

    def subtract(self):
        return self.v1-self.v2

    def setV1(self, v): # 1. setV1으로 들어온 변수 v의 데이터 타입을 체크한다.
        # if문을 사용.
        if isinstance(v, int): # = 만약 v가 숫자라면, int는 정수에대한 파이썬 내장 클래스
                               # isinstance(변수_명, 데이터_타입) => 해당 변수가 데이터_타입인지 알 수 있는 파이썬 내장함수 true or false를 리턴한다.
            self.v1 = v

    def getV1(self):
        #
        return self.v1, self.v2 # 값을 튜플형으로 보여줌.

# Main
c1 = Cal1(10,10)
print(c1.add())
print(c1.subtract())

c1.setV1('one')
c1.v2 = 30
print(c1.getV1()) # 실행결과 (10, 30) => v1은 int이기 때문에 one으로 바뀌지 않았다.
print(c1.add())
print(c1.subtract())

# 통합개발환경에서는 이러한 Set/Get 메소드를 자동으로 만들어주는 기능을 제공한다.
# 다음 파일에서 정리.