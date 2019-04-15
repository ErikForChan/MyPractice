#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/11 17:52
# software: PyCharm

# 冒泡
def buuble_sort(data):
    length = len(data)
    for count in  range(length-1):
        for index in range(length-1-count):
            if data[index] > data[index+1]:
                data[index],data[index+1] = data[index+1],data[index]

# 插入  从第2个元素开始，与前面所有元素n进行比较，如果n大于当前元素，则将n赋值给n的后一个值，最后将当前元素赋值给第n个元素，插入扑克牌
def insert_sort2(data):
    length = len(data)
    for count in range(1,length):
        cur = data[count]
        loc = count - 1
        while loc > -1 and data[loc] > cur:
            data[loc+1] = data[loc]
            loc -= 1
        data[loc+1] = cur


def insert_sort(data):
    length = len(data)
    for count in range(length):
        cur = data[count]
        for index in range(0,count):
            if cur < data[index]:
                data[count],data[index] = data[index],data[count]

data = [3,5,77,6,7,22,2,9,8]
insert_sort2(data)
print(data)

