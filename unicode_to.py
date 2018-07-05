#coding:utf-8
import pymongo
import json
import ast

client = pymongo.MongoClient('mongodb://localhost:27017')
db_name = 'a_information'
db = client[db_name]
collection_set01 = db['information']
# collection_set01.save()


# Python 字典类型转换为 JSON 对象
data = '''{'no' : 1,'name' : 'Runoob','url' : 'http://www.runoob.com'}'''
dd = eval(data)
print(dd)
print(type(dd))

f = open('information.txt')
line = f.readline()
line1 = line.strip(',')
a = eval(line)
print(type(a))
line2 = f.readline()
print("=====", type(line2))
bb = line2[:-2]
#print(bb)
line3 = f.readline()
print("=====", type(line3))
cc = line3[:-2]
dd = eval(cc)
collection_set01.save(dd)
print(type(dd))
# while line:
#     c = ast.literal_eval(line.decode('utf-8'))
#     print(c)
#     line = f.readline()