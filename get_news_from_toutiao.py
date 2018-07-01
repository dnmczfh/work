# coding：utf-8
import requests
import json
import pandas


url = 'http://www.toutiao.com/api/pc/focus/'
wbdata = requests.get(url).text

data = json.loads(wbdata)
news = data['data']['pc_feed_focus']

#遍历取得的数据
# for x in news:
#     print(x, '\n')
#     for key in x:
#         print(key+':'+str(x[key]))
#     print('\n')

news_data = []
for n in news:
    title = n['title']
    img_url = 'http:'+n['image_url']
    display_url='https://www.toutiao.com'+n['display_url'].replace('group/','a')
    result = {
        'title': title,
        'url': display_url,
        'image_url': img_url
    }
    print(result)
    news_data.append(result)

# df = pandas.DataFrame(news)
# df.to_excel('toutiao_news_source.xlsx')

df = pandas.DataFrame(news_data)
df.to_excel('toutiao_news.xlsx')

