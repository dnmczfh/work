import requests
import lxml
from bs4 import BeautifulSoup
from datetime import datetime
import pandas


res = requests.get('http://www.news.cn/politics/')
res.encoding='utf-8'
soup = BeautifulSoup(res.text,'lxml')
#print(soup)

scroll_list = BeautifulSoup(str(soup.find("div", attrs = "id": "hideData0")), "lxml")

soup = soup.select('.con')

print(soup)