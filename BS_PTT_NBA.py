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
    paging = soup.find('div', 'btn-group btn-group-paging').find_all('a')[1]['href']

    articles = []
    rents = soup.find_all('div', 'r-ent')
    for rent in rents:
        title = rent.find('div', 'title').text.strip()
        count = rent.find('div', 'nrec').text.strip()
        date = rent.find('div', 'meta').find('div', 'date').text.strip()
        article = '%s %s:%s' % (date, count, title)
