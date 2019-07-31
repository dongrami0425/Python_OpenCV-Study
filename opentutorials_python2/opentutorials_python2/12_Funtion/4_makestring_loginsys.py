
def login(login_id):
    members = ['dongmin', 'ldm8191', 'wmdmfh']
    for member in members:
        if member == login_id:
            return True

    return False

input_id = input("아이디를 입력해주세요.\n")

if login(input_id):
    print('Hello, '+input_id)
else:
    print('Who are you?')
