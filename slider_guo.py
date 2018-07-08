# -*- coding: UTF-8 -*-
from urllib import request
from lxml import etree
import requests
import pymongo
import time

client = pymongo.MongoClient('mongodb://localhost:27017')
db_name = 'a_information'
db = client[db_name]
collection_set01 = db['avmei']

url = "http://www.hmrenti.com/fanhao"
urll = "http://www.hmrenti.com/"
uurl = "http://www.hmrenti.com/fanhao/"

def qwer(uu):
    response = requests.get(url=uu)
    res = response.content.decode("gbk",'ignore')
    html = etree.HTML(res)
    list1 = html.xpath('//*[@id="wrapper980"]/table/tbody/tr/td[2]/a/@href')

    actor = html.xpath('//*[@id="wrapper980"]/table/tbody/tr/td[4]/text()')
    name = html.xpath('//*[@id="wrapper980"]/table/tbody/tr/td[2]/a/text()')
    time = html.xpath('//*[@id="wrapper980"]/table/tbody/tr/td[3]/text()')
    number = html.xpath('//*[@id="wrapper980"]/table/tbody/tr/td[1]/a/text()')
    create = html.xpath('//*[@id="wrapper980"]/table/tbody/tr/td[5]/text()')
    for j in range(0, len(list1)):
        response = requests.get(url=urll+list1[j])
        res = response.content.decode("gbk", 'ignore')
        html = etree.HTML(res)
        imgsrc = html.xpath('//*[@id="content"]/div[2]/img/@src')
        dict1={
            "name": name[j],
            "actor": actor[j],
            "create_time": create[j],
            "time": time[j],
            "number": number[j],
            "img": imgsrc[0]
        }
        collection_set01.save(dict1)

for i in range(1,100):
    if(i == 1):
        qwer(uu=url)
    else:
        time.sleep(1)
        url1 = uurl + str(i) +'.html'
        qwer(uu=url1)