from bs4 import BeautifulSoup


from bs4 import BeautifulSoup
from selenium import webdriver
import soupsieve

try:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    chrome = webdriver.Chrome(options=options, executable_path='chromedriver.exe')
    chrome.set_page_load_timeout(10)
    chrome.get('https://code-gym.github.io/spider_demo/')
    soup = BeautifulSoup(chrome.page_source, 'html5lib')
    print(soup.find('h1').text)
finally:
    chrome.quit()