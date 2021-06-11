import requests
from bs4 import BeautifulSoup
webpage = requests.get("https://m.blog.naver.com/SympathyHistoryList.naver?blogId=folkslife&logNo=222390678309&categoryId=POST")
soup = BeautifulSoup(webpage.content, "html.parser")
print(soup)