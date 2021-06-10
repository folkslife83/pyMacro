import urllib.request
from bs4 import BeautifulSoup
 
url = "https://m.blog.naver.com/SympathyHistoryList.naver?blogId=folkslife&logNo=222389312712&categoryId=POST"
req = urllib.request.Request(url)
sourcecode = urllib.request.urlopen(url).read()
soup = BeautifulSoup(sourcecode, "html.parser")

print(soup.prettify())