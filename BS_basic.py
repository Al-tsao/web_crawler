import requests
from bs4 import BeautifulSoup

resp = requests.get('https://code-gym.github.io/spider_demo/')
soup = BeautifulSoup(resp.text, 'html5lib')

#用標籤找資料
##使用find只會到第一個標籤的內容
print(soup.find('h1')) #使用find找到標籤中的內容，回傳內容會包含整個標籤
print(soup.find('h1').text) #將上text單純取得標籤中的文字
print(soup.h1) #可以簡化成這樣
print(soup.h1.text) #可以簡化成這樣
##使用find_all會把所有用該標籤的元素，然後以list的方式回傳，可以搭配迴圈把內容拿出來
for h3 in soup.find_all('h3'):
    #往標籤下層尋找
    ##可以在回傳的物件中加入想要搜尋的下層標籤，這樣就可以看到只想要的內容
    print(h3.a)
    #往標籤下層尋找

#用class取得網頁中元素資料
for title in soup.find_all('h3', 'post-title'):
    print(title.a)
