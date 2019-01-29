#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/22 15:08
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


def shif_heap_max(data,start,end):
    root = start
    while True:
        # 从root开始对最大堆调整
        child = 2 * root + 1
        # 如果没有子节点，则跳出循环
        if child > end:
            break
        # 如果存在右子节点，且左子节点小于右子节点，则将子节点设置为右子节点
        if child + 1 <= end and data[child] < data[child + 1]:
            child += 1
        # 如果子节点大于父节点，则交换他们的值
        if data[child] > data[root]:
            data[child],data[root] = data[root],data[child]
            root = child  # 并将父节点索引设置为子节点的索引
        else:
            break


def heap_sort(data):
    # 获取列表的长度
    size = len(data)
    # 构造一个大顶堆，从最后一个元素开始
    for i in range(int((size-2/2)),-1,-1):
        shif_heap_max(data,i,size-1)
    # 从最后一个元素开始循环
    for j in range(size-1,0,-1):
        # 将当前元素与第一个元素互换
        data[0],data[j] = data[j],data[0]
        # 将当前元素之前的所有元素构造出一个大顶堆
        shif_heap_max(data, 0, j - 1)


@count_time
def heap_test():
    # 无序列表
    data = [12, 5, 78, 9, 98, 17, 905]
    print(data)
    # 对列表进行堆排序
    heap_sort(data)
    print(data)


if __name__ == "__main__":
    heap_test()
