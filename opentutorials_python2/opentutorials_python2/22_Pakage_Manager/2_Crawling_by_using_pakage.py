# < Python의 패키지 메니저를 이용해서 크롤링하는 방법 >

# 크롤링 이란?[참고]
# - Web상에 존재하는 Contents를 수집하는 작업 (프로그래밍으로 자동화 가능)
# - HTML 페이지를 가져와서, HTML/CSS등을 파싱(parsing)하고, 필요한 데이터만 추출하는 기법
# - !!! Open API(Rest API)를 제공하는 서비스에 Open API를 호출해서, 받은 데이터 중 필요한 데이터만 추출하는 기법
# - Selenium등 브라우저를 프로그래밍으로 조작해서, 필요한 데이터만 추출하는 기법

# [ 크롤링에서 필요한 패키지 설치 ]
# 크롬에서 "python3 http download library" 검색 
# 사용법이 제시된 문서를 골라서 사용법을 확인한다.
# pip install requests => 패키지 설치 명령어

# 크롤링 예제에 사용하는 URL : https://codingeverybody.github.io/scraping_sample/1.html
# 웹페이지를 다운로드 하여 데이터를 사용해보자

import requests
from bs4 import BeautifulSoup

r = requests.get('https://codingeverybody.github.io/scraping_sample/1.html')
print(r.text)

# 출력결과
'''
<!doctype html>
<html>
 <head>
  <title>sample1</title>
 </head>
 <body>
  <div class="em">important information 1</div>
 </body>
</html>
'''

# 이제 가져온 정보를 분석해보자.
# 크롬에서 python3 html parser library 검색 => 분석에 필요한 라이브러리 정보를 알아본다.
# Beautiful Soup Documentation 을 통해 사용법, 설치법 확인
#  (또는 pypi 사이트에 들어가서 Beautiful soup를 인스톨하는법 확인.)
# python3에서 설치 명령어 : pip install beautifulsoup4

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.title) #타이틀 태그를 출력

print('Title : '+soup.title.string) # 타이틀 태그의 내용만 출력

articles = soup.findAll('div', {'class' : 'em'}) # soup.findAll() 은 해당 사이트의 어떤 조건의 모든 정보를 볼수 있는 명령어
                                                     # div태그에서 클래스가 em인 정보를 모두 보여줌.
print(articles)    # 리스트 형으로  값이 저장됨. 
print(articles[0]) # 첫번째 요소만 보는것.
print('Article : '+ articles[0].text) # .text를 붙이면 태그를 제외하고 내용만 text형식으로 보여줌.

# 다른 url정보도 확인해보자.
print('='*50)
r = requests.get('https://codingeverybody.github.io/scraping_sample/2.html')
soup = BeautifulSoup(r.text, 'html.parser')
print('Title : '+soup.title.string) 
articles = soup.findAll('div', {'class' : 'strong'})
print('Article : '+articles[0].text)


# 추가적인 웹크로링 공부 => 웹크롤링 기본 : https://www.fun-coding.org/crawl_basic3.html
