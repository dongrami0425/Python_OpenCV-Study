#2. @classmethod와 @staticmethod 의 차이
#classmethod와 static메소드의 차이는 상속에서 두드러지게 차이가 납니다.

class Language:
      default_language = "English"
    
      def __init__(self):
          self.show = '나의 언어는' + self.default_language
    
      @classmethod
      def class_my_language(cls):
          return cls()
    
      @staticmethod
      def static_my_language():
          return Language()
    
      def print_language(self):
          print(self.show)
    
    
class KoreanLanguage(Language):
      default_language = "한국어"


a = KoreanLanguage.static_my_language()
b = KoreanLanguage.class_my_language()
 
a.print_language()
 # 나의 언어는English
 
b.print_language()
 # 나의 언어는한국어

 # static method 와 classmethod는 모두 클래스 멤버이다.
 # staticmethod에서는 부모클래스의 클래스속성 값(클래스 변수)을 가져오지만, 
 # classmethod에서는 cls인자를 활용하여 cls의 클래스 속성 값(클래스 변수)을 가져오는 것을 알 수 있습니다.