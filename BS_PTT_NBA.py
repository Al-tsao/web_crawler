import requests
from bs4 import BeautifulSoup
import time

today = time.strftime('%m/%d').lstrip('0') #利用time模組取的時間字串

def pttNBA(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        print('URL發生錯誤' + url)
        return
    
    soup = BeautifulSoup(resp.text, 'html5lib') #利用html5lib解析文檔
    paging = soup.find('div', 'btn-group btn-group-paging').find_all('a')[1]['href'] #使用[]獲得屬性內容，使用.text獲得內文

    articles = []
    rents = soup.find_all('div', 'r-ent')
    for rent in rents:
        title = rent.find('div', 'title').text.strip()
        count = rent.find('div', 'nrec').text.strip()
        date = rent.find('div', 'meta').find('div', 'date').text.strip()
        article = '%s %s:%s' % (date, count, title)

        try:
            if today == date and int(count) > 10:
                articles.append(article)
        except:
            if today == date and count == '爆':
                articles.append(article)

    for article in articles:
        print(article)

    # if len(articles) != 0:
    #     for article in articles:
    #         print(article)
    #     pttNBA('https://www.ptt.cc' + paging)
    # else:
    #     return

pttNBA('https://www.ptt.cc/bbs/NBA/index.html')