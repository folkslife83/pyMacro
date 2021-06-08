import urllib.request
from bs4 import BeautifulSoup
 
url = "https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=recentdate&keyword=%EB%A7%88%EA%B3%A1"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='title')
#title = soup.findAll('span', attrs= {'class' :'title'})
print(title)
