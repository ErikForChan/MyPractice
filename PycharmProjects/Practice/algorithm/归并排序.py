#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/23 12:59
# software: PyCharm
import datetime


def count_time(func):
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        result = func(*args, **kwargs)
        over_time = datetime.datetime.now()   # 程序结束时间
        total_time = (over_time-start_time).total_seconds()
        print('程序共计%s秒' % total_time)
        return result
    return int_time


# 将数据两个两个排好序，再四个四个拍好序，依次类推
def merge(lst,start,mid,end):
    # lst = [1,4,5,6,2,3,7,8,9]
    # merge(lst, 0, 3, len(lst) - 1)
    low = start
    high = mid + 1
    newList = []
    while low <= mid and high <= end:
        if lst[low] < lst[high]:
            newList.append(lst[low])
            low += 1
        else:
            newList.append(lst[high])
            high += 1
    while low <= mid:
         newList.append(lst[low])
         low += 1
    while high <= end:
         newList.append(lst[high])
         high += 1

    lst[start:end+1] = newList


def merge_sort(lst,start,end):
    if start < end:
        mid = (start + end)//2 # /得到浮点数，//得到整数
        merge_sort(lst,start,mid)
        merge_sort(lst, mid+1, end)
        merge(lst,start,mid,end)


if __name__ == "__main__":
    lst = [34,23,67,1,9,7,56,76,11]
    merge_sort(lst,0,len(lst)-1)
    # merge(lst,0,3,len(lst)-1)
    print(lst)