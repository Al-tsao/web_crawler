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
    for i in range (i,9):
        _url = url + str(i)
        print(_url)
finally: