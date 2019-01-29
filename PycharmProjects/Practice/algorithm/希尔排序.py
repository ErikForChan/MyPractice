#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/23 16:27
# software: PyCharm
import scrapy
def shell_sort(lst):
    # lst = [3, 23, 67, 1, 9, 7, 56, 76, 11]
    length = len(lst)
    gap = length//2
    while gap >= 1:
        for i in range(gap,length):
            temp = lst[i]
            j = i - gap
            while j >= 0 and lst[j] > temp:
                lst[j + gap] = lst[j]
                j -= gap
            lst[j+gap] = temp
            # lst[i - gap] = temp
        gap //= 2



if __name__  == "__main__":
    lst = [53, 23, 67, 1, 9, 7, 56, 76, 11]
    shell_sort(lst)
    print(lst)
