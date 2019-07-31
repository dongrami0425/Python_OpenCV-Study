# 로그인 애플리케이션에 입력기능 추가하기
in_str = input("아이디를 입력해주세요.\n") #아이디를 입력함수로 값을 설정.
real_dongmin = "ldm8191"
real_lee = "deokbae"
if real_dongmin == in_str:
  print("Hello!, donmin")
elif real_lee == in_str:
  print("Hello!, LEE")
else:
  print("Who are you?")