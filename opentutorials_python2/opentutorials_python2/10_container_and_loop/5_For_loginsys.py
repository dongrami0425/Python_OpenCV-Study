
input_id = input("아이디를 입력해주세요.\n") #입력함수
members = ['dongmin', 'ldm8191', 'leezche']
for member in members:
    if member == input_id: #입력함수와 for문마다 member의 값과 대조하며 일치할때 프린트함수가 출력됨.
        print('Hello!, '+member)
        import sys # 아이디가 맞으면 출력후 끝내기 위해 sys를 사용.
        sys.exit() # system이 종료되는 함수.
print('Who are you?')

