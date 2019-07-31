# < 클래스 변수 >
#  클래스 멤버로서 클래스 내에서 사용되는 지역변수.


class Cs2:
    count = 0            # 4. __init__에서 사용된 Cs.count가 명확하게 정의되지 않으면 에러
                         #    클래스의 내부 and 메소드의 바깥에서 클래스안에서 사용되는 지역변수를 선언해줘야 한다.
                         #    즉, 메소드 안에서 "클래스_명.변수_명" 은 클래스 변수이며   변수_명을 클래스지역변수로 선언및 초기화 해야한다.
    def __init__(self):
        Cs.count = Cs.count + 1 # 1. 인스턴스가 생성될때 마다 생성된 횟수를 카운트.

    @classmethod        # 2. @classmethod  => "클래스에 소속된 메소드이며 클래스멤버이다." 를 선언해줌.
    def getCount(cls):  # 3, cls : 클래스 메소드의 경우 첫번째 매개변수가 "cls" 이다. self처럼 메소드가 소속된 클래스를 가리키는 값을 첫번째 매개변수로 약속되어 있다.
        return Cs.count #       => 따라서 return Cs.count는 return cls.count로 사용할 수 있다. 
                        


i1 = Cs2()
i2 = Cs2()
i3 = Cs2()
i4 = Cs2()
print(Cs.getCount())