#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2018/12/28 10:29
# software: PyCharm

import re
from day5ATM.Calculator.MD import multdiv

expression = input()
members = re.findall('([\d\.]+|/|-|\+|\*)',expression)
print(members)


def function(members):
    sum = 0
    while 1:
        if '*' in members and '/' not in members:
            multdiv(members,'*')
        elif '/' in members and '*' not in members:
            multdiv(members, '/')
        elif '/' in members and '*' in members:
            mIndex = members.index('*')
            dIndex = members.index('/')
            if mIndex < dIndex:
                multdiv(members, '*')
            else:
                multdiv(members, '/')
        else:
            if members[0] == '-':
                members[0] = members[0] + members[1]
                del members[1]
            sum += float(members[0])
            for i in range(1,len(members),2):
                if members[i] == '+' and members[i+1] != '-':
                    sum += float(members[i+1])
                elif members[i] == '+' and members[i+1] == '-':
                    sum += -(float(members[i + 2]))
                elif members[i] == '/' and members[i+1] != '-':
                    sum -= float(members[i + 1])
                elif members[i] == '/' and members[i+1] == '-':
                    sum -= -(float(members[i+2]))
            break
    return sum


def calculate(expression):
    loc = []
    ans = 0
    if '(' not  in expression:
        ans = function(expression)
        return ans
    for i in range(expression):
        if expression[i] == '(':
            loc.append(i)
        elif expression[i] == ')':
            tempRes = 0
            sub = expression[loc[len(loc)-1]:i]
            tempRes = function(sub)
            expression = expression[0:loc[len(loc)-1]]+str(tempRes)+expression[i+1:len(expression)+1]
            loc.pop()
            return calculate(expression)


a = calculate(members)
print(a)
