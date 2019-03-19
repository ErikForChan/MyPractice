#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/17 18:41
# software: PyCharm
import os
import json
loginUI = '''
-----------------欢迎光临智能ATM机------------------
-----------------请输入密码登陆------------------
'''
# 获取当前文件的父目录文件夹
ATM_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def login(userDic):
    print(loginUI)
    login_info = {}
    login_status = False
    while True:
        username = input("用户名：")
        password = input("密码：")
        if username in userDic:
            pwd = userDic[username]["password"]
            if str(password) == str(pwd):
                print("\033[32;1m登陆成功，欢迎[ %s ]\033[0m" % username)
                login_status = True
                break;
            else:
                print("\033[31;1m密码错误\033[0m")
        else:
            print("\033[31;1m用户名不存在\033[0m")
            print("\033[34;1m请重新登陆！！！\033[0m", end='\n')
    login_info["status"] = login_status
    login_info["username"] = username
    return login_info
