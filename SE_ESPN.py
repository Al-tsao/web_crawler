from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random

url = 'https://insider.espn.com/nba/hollinger/statistics/_/page/1'

try:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    chrome = webdriver.Chrome(options=options, executable_path='chromedriver.exe')
    chrome.set_page_load_timeout(10)
    for i in range (1, 9):
        _url = url + str(i)
        print(_url)
        chrome.get(_url)
        soup = BeautifulSoup(chrome.page_source, 'html5lib')
        trs = soup.find('tbody').find_all('tr')
        for tr in trs:
            tds = [td for td in tr.children]
            rk = tds[0].text.strip()
finally: