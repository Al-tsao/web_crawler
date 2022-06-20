import requests
from bs4 import BeautifulSoup
import time

url = 'https://tip.railway.gov.tw/tra-tip-web/tip'
staDic = {}
today = time.strftime('%Y/%m/%d')
sTime = '06:00'
eTime = '12:00'

def getTrip():
    resp = requests.get(url)
    if resp.status_code != 200:
        print('URL發生錯誤' + url)
        return

    soup = BeautifulSoup(rep.text, 'html5lib')