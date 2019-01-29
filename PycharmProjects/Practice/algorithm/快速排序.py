#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/21 15:42
# software: PyCharm
import random
import datetime
# import sys
# sys.setrecursionlimit(1000000) #例如这里设置为一百万

data = list(range(1000))
random.shuffle(data)


def count_time(func):
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        result = func(*args, **kwargs)
        over_time = datetime.datetime.now()   # 程序结束时间
        total_time = (over_time-start_time).total_seconds()
        print('程序共计%s秒' % total_time)
        return result
    return int_time


# 快速排序，选一个元素，将列表中的其他元素，大的放在此元素后面，小的放在前面 nLog(n) 或者 n^2
# 整理 递归
def quikc_sort(lst,left,right):
    if left<right:
        mid = partition(lst,left,right)
        quikc_sort(lst, left, mid-1)
        quikc_sort(lst, mid + 1, right)
# data = [3,5,1,6,7,4,2,9,8]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def partition(lst,left,right):
    temp = lst[left]
    while left < right:
        while left < right and lst[right] >=temp:
            right -= 1
        lst[left] = lst[right]
        while left<right and lst[left] <= temp:
            left += 1
        lst[right] = lst[left]
    lst[left] = temp
    return left


@count_time
def quick_sort(lst,left,right):
    return quikc_sort(lst,left,right)


quick_sort(data,0,len(data)-1)
print(data)