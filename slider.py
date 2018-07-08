# -*- coding: UTF-8 -*-
from urllib import request
from lxml import etree
import requests
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
db_name = 'a_information'
db = client[db_name]
collection_set01 = db['avJing']

list1 = [19,19,14,14,14,11,13,13,8,10,13,14]
url = "https://www.fan81.com/fan"

def qwer(uu):
    response = requests.get(url=uu)
    res = response.content.decode("utf-8")
    html = etree.HTML(res)
    imgsrc = html.xpath('//*[@id="main"]/div/div[2]/ul/li/h3/a/img/@src')
    time = html.xpath('//*[@id="main"]/div/div[2]/ul/li/h3/a/span/text()')
    name = html.xpath('// *[ @ id = "main"]/div/div[2]/ul/li/div/header/h3/a/text()')
    create_time = html.xpath('//*[@id="main"]/div/div[2]/ul/li/div/header/p/span/span[2]/text()')
    actor = html.xpath('//*[@id="main"]/div/div[2]/ul/li/div/p/span[1]/text()')
    publisher = html.xpath('//*[@id="main"]/div/div[2]/ul/li/div/p/span[2]/text()')
    number = html.xpath('//*[@id="main"]/div/div[2]/ul/li/div/p/span[3]/text()')
    length = len(time)
    for i in range(0,length):
        dict1={
            "name": name[i],
            "actor": actor[i],
            "create_time": create_time[i],
            "time": time[i],
            "number": number[i],
            "img": "https://www.fan81.com/"+imgsrc[i]
        }
        collection_set01.save(dict1)

for i in range(1,13):
    if(i == 1):
        urll = url + str(i) + '/index.html'
        qwer(uu=urll)
    else:
        for j in range(2,list1[i-1]):
            urll = url + str(i) + '/index_' + str(j)+'.html'
            qwer(uu=urll)


