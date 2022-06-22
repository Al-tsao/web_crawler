import requests
from bs4 import BeautifulSoup
import time
import datetime

url = 'https://tip.railway.gov.tw/tra-tip-web/tip'
staDic = {}
today = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y/%m/%d')
sTime = '06:00'
eTime = '12:00'

def getTrip():
    resp = requests.get(url)
    if resp.status_code != 200:
        print('URL發生錯誤' + url)
        return

    soup = BeautifulSoup(resp.text, 'html5lib')

    stations = soup.find(id = 'cityHot').ul.find_all('li')
    for station in stations:
        stationName = station.button.text
        stationId = station.button['title']
        staDic[stationName] = stationId

    csrf = soup.find(id = 'queryForm').find('input',{'name':'_csrf'})['value']

    formData = {
        'trainTypeList':'ALL',
        'transfer':'ONE',
        'startOrEndTime':'true',
        'startStation':staDic['臺北'],
        'endStation':staDic['新竹'],
        'rideDate':today,
        'startTime':sTime,
        'endTime':eTime, 
        '_csrf':csrf
    }


getTrip()