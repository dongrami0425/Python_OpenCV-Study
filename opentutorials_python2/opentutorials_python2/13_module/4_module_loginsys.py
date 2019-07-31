import auth # 모듈을 불러오는 것으로 메인의 코드가 간결해지며 중복의 제거가 가능.

input_id = input("아이디를 입력해주세요.\n")
if auth.login(input_id):
    print('Hello, '+input_id)
else:
    print('Who are you?')

