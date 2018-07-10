import requests
from lxml import etree
import re
import pymongo
import datetime
import time

client = pymongo.MongoClient('mongodb://localhost:27017')
db_name = 'weibo'
db = client[db_name]
collection_set01 = db['hot_list']
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
headers = {user_agent: user_agent}
while 1 == 1:
    res = requests.get('http://s.weibo.com/top/summary?cate=realtimehot', headers=headers)
    con = res.content.decode('utf-8')
    html = etree.HTML(con)
    list1 = html.xpath('//script[10]/text()')
    str1 = str(list1[0]).split("(", 1)
    html1 = eval(str1[1][:-1])['html']
    link_list = re.findall('\/wei.*=top', str(html1))
    number_lsit = re.findall('num"><span>.*<', str(html1))
    for i in range(0, len(link_list)):
        link_list[i] = "http://s.weibo.com" + link_list[i][:6] + link_list[i][7:]

    for i in range(0, 50):
        res = requests.get(link_list[2 * i], headers=headers)
        con = res.content.decode('utf-8')
        name = re.findall('<title>微博搜索 - .* - 微博</title>', con)
        one = collection_set01.find_one({"content": name[0][13:][:-13]})
        if not one:
            dic = {
                "content": name[0][13:][:-13],
                "links": link_list[2 * i],
                "hot": [{"order": i + 1, "hhot": re.findall('(\d+)', number_lsit[i])[0],
                         "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]
            }
            collection_set01.save(dic)
        else:
            one['hot'].append({"order": i + 1, "hhot": re.findall('(\d+)', number_lsit[i])[0],
                               "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            two = collection_set01.update({"content": name[0][13:][:-13]}, one)
    time.sleep(600)
    aaa