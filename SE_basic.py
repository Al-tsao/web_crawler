from bs4 import BeautifulSoup


from bs4 import BeautifulSoup
from selenium import webdriver
import soupsieve

try:
    chrome = webdriver.Chrome(executable_path='chromedriver.exe')
    chrome.set_page_load_timeout(10)
    chrome.get('https://code-gym.github.io/spider_demo/')
    soup = BeautifulSoup(chrome.page_source, 'html5lib')
    print(soup.find('h1').text)
finally:
    chrome.quit()