import requests
from lxml import etree
import re
import pymongo
import time

client = pymongo.MongoClient('mongodb://localhost:27017')
db_name = 'weibo'
db = client[db_name]
collection_set01 = db['hot_list']

while 1 == 1:
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    headers = {user_agent: user_agent}
    res = requests.get('http://s.weibo.com/top/summary?cate=realtimehot', headers=headers)
    con = res.content.decode('utf-8')
    html = etree.HTML(con)
    list1 = html.xpath('//script[10]/text()')
    str1 = str(list1[0]).split("(", 1)
    html1 = eval(str1[1][:-1])['html']
    link_list = re.findall('\/wei.*=top', str(html1))
    name_list = re.findall('hot">.*a>', str(html1))
    number_lsit = re.findall('num"><span>.*<', str(html1))
    print(len(number_lsit), number_lsit)
    for i in range(0, len(link_list)):
        link_list[i] = "http://s.weibo.com" + link_list[i][:6] + link_list[i][7:]
    print(link_list)
    content_list = []
    for j in range(0, 50):
        name_list[2 * j] = name_list[2 * j][5:][:-5]
        content_list.append(name_list[2 * j])

    for i in range(0, 50):
        dic = {
            "content": content_list[i],
            "links": link_list[2 * i],
            "order": i + 1,
            "hot": re.findall('(\d+)', number_lsit[i])[0]
        }
        collection_set01.save(dic)
        print(dic)
    time.sleep(600)