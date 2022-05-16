import re
import requests
from bs4 import BeautifulSoup

resp = requests.get('https://code-gym.github.io/spider_demo/')
soup = BeautifulSoup(resp.text, 'html5lib')
print(soup.find('h1')) #使用find找到標籤中的內容，回傳內容會包含整個標籤
print(soup.find('h1').text) #將上text單純取得標籤中的文字
