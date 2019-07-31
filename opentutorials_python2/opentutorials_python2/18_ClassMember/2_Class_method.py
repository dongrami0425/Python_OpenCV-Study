# < 클래스 메소드 >
# 파이썬 에서는 클래스 멤버에 해당되는 메소드는 두종류이다. static 과 class 메소드이다.
# 두 메소드의 차이는 추후에 설명.
# 클래스 메소드는 클래스의 소속으로 사용되는 것, 인스턴스 메소드는 인스턴스의 소속으로 사용되는 것.

class Cs:            
    @staticmethod # 1. @(장식자)  # 2. @stacicmethod => "클래스에 소속된 메소드이며 클래스멤버이다." 를 선언해줌.
    def static_method():
        print("Static method")

    @classmethod                    # 3. @classmethod  => "클래스에 소속된 메소드이며 클래스멤버이다." 를 선언해줌.
    def class_method(cls):          # cls : 클래스 메소드의 경우 첫번째 매개변수가 "cls" 이다.
        print("Class method")

    def instance_method(self):
        print("Instance method")

i = Cs()
Cs.static_method() # => 
Cs.class_method()
i.instance_method()
