#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/3/26 10:28
# software: PyCharm
# List,tuple查询速度相对慢，不能储存关联性较强的数据。
# 字典的查询速度很快，遵循哈希算法。
# 字典的键不能重复

dict = {
    "name":"lily",
    "age":100,
    "city":"New York"
}
dict['gender'] = "femal"
# dict.setdefault("haha","231")
# del dict['age']
# dict1 = {
# "name":"lily12",
#     "tall":"190cm"
# }
# dict.update(dict1)
# ret = dict.get("name")
# print(ret)
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# dict1 = {}
# dict1 = dict1.fromkeys([1,2,3],"aa")
print(dict)

# 在循环一个字典的时候，不能改变字典的长度
# 	如果要删除某些键值对，可将键存入列表。




