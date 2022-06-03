import requests
from bs4 import BeautifulSoup
import time

today = time.strftime('%m/%d').lstrip('0') #利用time模組取的時間字串

def pttNBA(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        print('URL發生錯誤' + url)
        return
    
    soup = BeautifulSoup(resp.text, 'html5lib')