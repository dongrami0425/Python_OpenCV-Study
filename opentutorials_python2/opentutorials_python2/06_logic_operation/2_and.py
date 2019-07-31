# AND
'''
False	and	 False	= False
False	and	 True	= False
True	and	 False	= False
True	and	 True	= True
'''

input_id = input("아이디를 입력해주세요.\n")
input_pwd = input("비밀번호를 입력해주세요.\n")
real_id = "ldm8191"
real_pwd = "asdf1234"

# 아이디와 패스워드가 둘다 맞아야만 로그인 성공.
if real_id == input_id and real_pwd == input_pwd:
    print("Hello!")
else:
    print("로그인에 실패했습니다")


