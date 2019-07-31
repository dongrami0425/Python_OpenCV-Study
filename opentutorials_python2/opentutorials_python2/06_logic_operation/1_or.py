# OR
'''
False	or	False	=False
False	or	True	=True
True	or	False	=True
True	or	True	=True
'''

in_str = input("아이디를 입력해주세요.\n") #아이디를 입력함수로 값을 설정.
real_dongmin = "ldm8191"
real_lee = "deokbae"
# 두명의 사용자가 로그인 하는 로직이었다.
# 둘중 한명이라도 로그인에 성공한다면 Hello! 출력
if (real_dongmin == in_str) or (real_lee == in_str) : 
  print("Hello!")
else:
    print("Who are you?")

