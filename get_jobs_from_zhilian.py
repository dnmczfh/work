
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import re
import time

def get_zhaopin_old(page):
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=深圳&kw=python&p={0}&kt=3'.format(page)
    print("第{0}页".format(page))
    wbdata = requests.get(url).content
    soup = BeautifulSoup(wbdata, 'lxml')

    job_name = soup.select("table.newlist > tr > td.zwmc > div > a")
    salarys = soup.select("table.newlist > tr > td.zwyx")
    locations = soup.select("table.newlist > tr > td.gzdd")
    times = soup.select("table.newlist > tr > td.gxsj > span")

    for name, salary, location, time in zip(job_name, salarys, locations, times):
        data = {
            'name': name.get_text(),
            'salary': salary.get_text(),
            'location': location.get_text(),
            'time': time.get_text(),
            'url': name['href']
        }
        print(data)

def get_zhaopin_1(page):
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=深圳&kw=python&p={0}&kt=3'.format(page)
    print("第{0}页".format(page))
    wbdata = requests.get(url).content
    soup = BeautifulSoup(wbdata, 'lxml')

    job_name = soup.select("table.newlist > tr > td.zwmc > div > a")
    salarys = soup.select("table.newlist > tr > td.zwyx")
    locations = soup.select("table.newlist > tr > td.gzdd")
    times = soup.select("table.newlist > tr > td.gxsj > span")

    for name, salary, location, time in zip(job_name, salarys, locations, times):

        url = name['href']
        wbdata = requests.get(url).content
        soup = BeautifulSoup(wbdata, 'lxml')
        gsmc = soup.select('div.inner-left > h2')
        if len(gsmc) > 0:
            company = gsmc[0].get_text()
        else:
            company =''

        data = {
            'name': name.get_text(),
            'company':company,
            'salary': salary.get_text(),
            'location': location.get_text(),
            'time': time.get_text(),
            'url': name['href']
        }
        print(data)

def get_zhaopin_2(page):
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=深圳&kw=python&p={0}&kt=3'.format(page)
    print("第{0}页".format(page))
    wbdata = requests.get(url).content
    soup = BeautifulSoup(wbdata, 'lxml')

    tagList = soup.select("table.newlist")
    for tag in tagList:
        # print(tag)
        x = tag.find('td', attrs={'class': 'zwmc'})
        # print(x)
        if not x is None:
            data = {
                'name': x.a.get_text().strip(),
                'company': tag.find('td', attrs={'class': 'gsmc'}).a.get_text().strip(),
                'salary': tag.find('td', attrs={'class': 'zwyx'}).get_text().strip(),
                'location': tag.find('td', attrs={'class': 'gzdd'}).get_text().strip(),
                'time': tag.find('td', attrs={'class': 'gxsj'}).get_text().strip(),
                'url': x.a.get('href')
            }
            print(data)


if __name__ == '__main__':

    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=深圳&kw=python&p=1&kt=3'
    wbdata = requests.get(url).content
    soup = BeautifulSoup(wbdata, 'lxml')

    items = soup.select("div#newlist_list_content_table > table")
    count = len(items) - 1
    # 每页职位信息数量
    print(count)

    job_count = re.findall(r"共<em>(.*?)</em>个职位满足条件", str(soup))[0]
    # 搜索结果页数
    pages = (int(job_count) // count) + 1
    print(pages)

    start = time.clock()
    pool = Pool(processes=2)
    pool.map_async(get_zhaopin_old, range(1, pages + 1))
    pool.close()
    pool.join()
    end = time.clock()
    print('Running time: %s Seconds'%(end-start))


