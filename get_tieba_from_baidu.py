from bs4 import BeautifulSoup

import requests
from mylog import MyLog as mylog


# 《Python 网络爬虫实战》胡松涛著 P196

class Item():
    title = None
    firstAuthor = None
    firstTime = None
    reNum = None
    content = None
    lastAuthor = None
    lastTime = None


class GetTiebaInfo():
    def __init__(self, url):
        self.url = url
        self.log = mylog()
        self.pageSum = 1
        self.urls = self.getUrls(self.pageSum)
        self.items = self.spider(self.urls)
        self.pipelines(self.items)

        # http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100

        ## http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0

    ## http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50
    ## http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100
    ## http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150
    ## http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=200
    def getUrls(self, pageSum):
        urls = []
        pns = [str(i * 50) for i in range(pageSum)]
        ul = self.url.split("=")
        for pn in pns:
            ul[-1] = pn
            url = "=".join(ul)
            print(url)
            urls.append(url)
        return urls

    def spider(self, urls):
        items = []
        for url in urls:
            htmlContent = self.getResponseContent(url)
            soup = BeautifulSoup(htmlContent, 'lxml')
            # 注意：这里前面有个空格
            tagsli = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})
            for tag in tagsli:
                item = Item()
                item.title = tag.find('a', attrs={'class': 'j_th_tit'}).get_text().strip()
                # 注意，这里有一个 .a
                item.firstAuthor = tag.find('span', attrs={'class': 'frs-author-name-wrap'}).a.get_text().strip()
                item.firstTime = tag.find('span', attrs={'title': '创建时间'}).get_text().strip()
                item.reNum = tag.find('span', attrs={'title': '回复'}).get_text().strip()
                # 注意：这里后面有个空格
                item.content = tag.find('div',
                                        attrs={'class': 'threadlist_abs threadlist_abs_onlyline '}).get_text().strip()
                item.lastAuthor = tag.find('span', attrs={'class': 'tb_icon_author_rely j_replyer'}).get_text().strip()
                item.lastTime = tag.find('span', attrs={'title': '最后回复时间'}).get_text().strip()
                items.append(item)
                self.log.info('获取标题为《%s》的项成功 ...' % item.title)
        return items

    def pipelines(self, items):
        fileName = '百度贴吧_python.txt'
        with open(fileName, 'w', encoding='utf-8') as fp:
            for item in items:
                fp.write(
                    'title:{} \t author:{} \t firstTime:{} \ncontent:{} \n return:{} \n lastAuthor:{} \t lastTime:{} \n\n\n\n'
                        .format(item.title, item.firstAuthor, item.firstTime, item.content, item.reNum, item.lastAuthor,
                                item.lastTime))

    def getResponseContent(self, url):
        try:
            response = requests.get(url)
        except:
            self.log.error('Python 返回 URL:%s 数据失败' % url)
        else:
            self.log.info('Python 返回 URL:%s 数据成功' % url)
            return response.text


if __name__ == '__main__':
    url = 'http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50'
    GTI = GetTiebaInfo(url)