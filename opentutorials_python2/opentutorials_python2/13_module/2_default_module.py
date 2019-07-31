import math # 파이썬에 디폴트로 내장된 모듈

print(math.ceil(2.2))  # 올림
print(math.floor(2.9)) # 소수점 이하를 모두 무시 
print(math.trunc(-3.14))#trunc()함수는 내림을 하더라도 0으로 향함, floor은 무조건 그아래 수를 향함
print(math.sqrt(16))   # 루트

#round는 파이썬에 내장된 함수.
print(round(3.5)) # 반올림.
print(round(34.1234123123, 2)) # 소수점 2째 자리까지 나타내고 3쨰자리에서 반올림.
print(round(34345.1234123123, -2)) # 정수자리를 반올림 할때는  -로 표현. 해당숫자자리에서 반올림.
