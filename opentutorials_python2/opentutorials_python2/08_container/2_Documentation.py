# 사용설명서 => 문서(Documentation)를 통해 사용법을 볼 수 있다.

'''
 - 입문서(Getting Started) : 처음 사용하는 자들이 보는 것
 - 자습서(Tutorial) : 입문서이면서 좀더 깊은 내용까지 아우르는 것.
 - 검색(Search) :
 - 참조(reference) : 어떤 자료의 구조를 파악하는 것이 중요. 그래야 레퍼런스를 통해 자신이 원하는 것을 찾아 해결하는 능력이 필요함.
  '''

  #사용설명서 보는법 과 리스트 심화.
  # 레퍼런스를 사용하는 법 / 레퍼런스를 이용해 리스트 사용하기.
'''
  Python3 Documentation URL : https://docs.python.org/3
  Language Reference :
  Library Reference : 리스트에 대한 내용을 찾아볼 수 있음.
  1) Built-in Types > Sequence Types - list, tuple, range 등이있음.
  2) list, tuple, range는 Sequence Types에 속해있음

  3) common sequence opration : 3개의 자료형이 가지는 공통기능
  4) 표를 보기힘들다면 아래로 스크롤을 내리면 예제들도 볼 수 있음.

  5) 또한 각각의 자료형이 가지는 추가적인 기능들도 있으니 해볼 것.


'''


al = ['A', 'B', 'C', 'D']

print(A in al) # al에 A가 있으면 True 없으면 false
print(A not in al) #al에 A가 있으면 false 없으면 True 

print(len(al)) # 4 : 리스트의 길이

al.append('E') # 리스트의 끝에 데이터를 추가하며 리스트를 확장.
print(al) #['A', 'B', 'C', 'D', 'E']

del(al[0]) # 리스트의 요소를 삭제함.
print(al) #['B', 'C', 'D', 'E']