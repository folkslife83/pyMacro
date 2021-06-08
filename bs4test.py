import requests
from bs4 import BeautifulSoup

url = 'https://m.blog.naver.com/SectionPostSearch.naver?orderType=date&searchValue=%EB%A7%88%EA%B3%A1'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
print(soup)