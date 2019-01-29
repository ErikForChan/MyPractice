#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2018/12/29 10:05
# software: PyCharm


class Human:
    def __init__(self):
        print("I'm human")


class Mother(Human):
    def __init__(self):
        print("I'm uncle")


class Father(Human):
    def __init__(self):
        print("I'm father")


class Son(Father,Mother):
    def __init__(self):
        print("I'm son")
