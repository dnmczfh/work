import requests
import pypandoc
import os
import shutil
from bs4 import BeautifulSoup
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

#获取解编码后的HTML
def get_html_soup(url):
    try:
        response = requests.get(url, timeout = 100)
        response.encoding = 'utf-8'
    except Exception as e:
        print(e, "please check your network situation")
        return None
    soup = BeautifulSoup(response.text, "lxml")
    return soup

#获取新闻的标题和正文链接
def get_title_link(url, pattern):
    soup = get_html_soup(url)

    news_link = {}

    for link in soup.select(pattern):
        if len(link.get_text().strip()) > 0 and link.get("href").find("http") != -1:
            news_link[link.get_text()] = link.get('href')
    return news_link

def get_news_body(url):#抓取新闻主体内容
    content_text = []
    article_div = ""
    soup = get_html_soup(url)
    print(soup)
    if soup == None:
        return None

    article_div = str(soup.find("div", attrs = {"class": "main-aticle"}))
    soup = BeautifulSoup(str(article_div), "lxml")
    for content in soup.find_all("p"):
        if len(content.get_text().strip()) > 0:
            content_text.append("    " + content.get_text().strip())

    for x in content_text:
        if x == "    None":
            return None

    return content_text

#构建新闻来源字典（可以存在在文件中）
#网址，选择方式，存储目标
source = {'xinhua':["http://www.news.cn/",'#focusItem a','新华网'],
          'sina':['http://news.sina.com.cn/china','.news-item','新浪网']}

url = source['xinhua'][0]
pattern = source['xinhua'][1]
#soup = get_html_soup(url)
news_link = get_title_link(url, pattern)

for x in news_link:
    print(x+':'+news_link[x])
