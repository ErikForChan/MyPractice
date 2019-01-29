#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/21 14:49
# software: PyCharm
import datetime
import random
# 有序区：0， 无序区：所有

data = [3,5,1,6,7,4,2,9,8]


def count_time(func):
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        result = func(*args, **kwargs)
        over_time = datetime.datetime.now()   # 程序结束时间
        total_time = (over_time-start_time).total_seconds()
        print('程序共计%s秒' % total_time)
        return result
    return int_time

# 如果前面的数比后面的数大，则交换位置,将大的数放在后面，有序区在最后
@count_time
def bubble_sort(lst):
    for i in range(len(lst)-1):
        exhange = False
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                exhange = True
        if not exhange:
            break


# 选择排序，一趟遍历记录最小的数，放到第一个位置
@count_time
def select_sort(lst):
    for i in range(len(lst) - 1):
        min_loc = i;
        for j in range(i+1,len(lst)):
            if lst[i] > lst[j]:
                min_loc = j
                # lst[i],lst[j] = lst[j],lst[i]
        if min_loc != i:
            lst[i], lst[min_loc] = lst[min_loc], lst[i]


# 插入排序，将元素与前面的数一个一个比较，并插入到合适的位置，和整理扑克牌一样
@count_time
def insert_sort(lst):
    for i in range(1,len(lst)):
        temp = lst[i]
        loc = i-1
        while loc > -1 and lst[loc] > temp:
            lst[loc+1] = lst[loc]
            loc = loc-1
        lst[loc + 1] = temp


data = list(range(1000))
random.shuffle(data)
print(data)
bubble_sort(data)
print(data)





