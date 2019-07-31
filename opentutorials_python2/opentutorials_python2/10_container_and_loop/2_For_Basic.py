# for문의 등장.


#i=0
#print(len(member)) # len(리스트변수) => 리스트의 길이값을 리턴해줌.

#while i<len(member):
#    print(member[i])
#    i=i+1

members = ['egoing', 'leezche', 'graphittie']
for member in members:  # for 변수 in 컨테이너_명 : 컨테이너안의 값을 for문이 반복마다 값을 꺼내서 변수에 대입하여 사용됨.
                        #                          더 이상 꺼내올 값이 없을때 까지 반복하고 종료됨.
    print(member)

