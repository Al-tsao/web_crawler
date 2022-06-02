import requests
from bs4 import BeautifulSoup
import time

today = time.strftime('%m/%d').lstrip('0') #利用time模組取的時間字串

print(today)