#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2018/12/28 10:32
# software: PyCharm


def multiply_divide(s):
    ret = float(s.split('*')[0]) * float(s.split('*')[1]) \
            if '*' in s else \
            float(s.split('/')[0]) / float(s.split('/')[1])
    return ret


def multdiv(arr,symbol):
    index = arr.index(symbol)
    if symbol == '*' and arr[index +1] != '-':
        result = float(arr[index - 1]) * float(arr[index + 1])
    elif symbol == '/' and arr[index +1] != '-':
        result = float(arr[index - 1]) / float(arr[index - 1])
    elif symbol == '*' and arr[index +1] == '-':
        result = -(float(arr[index - 1]) * float(arr[index + 2]))
    elif symbol == '/' and arr[index + 1] == '-':
        result = -(float(arr[index - 1]) / float(arr[index + 2]))
    del arr[index - 1],arr[index - 1],arr[index - 1]
    arr.insert(index-1,str(result))
    return arr