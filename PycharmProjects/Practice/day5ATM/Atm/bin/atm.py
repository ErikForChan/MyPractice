#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/10 17:02
# software: PyCharm

import os
import json
import sys
from day5ATM.Atm.bin import tools
from day5ATM.Atm.core import login,transaction

print(sys.path)

mainUI = '''
-----------------欢迎光临智能ATM机------------------
----------------------请选择操作--------------------
1、存钱
2、取钱
3、转账
----------------------------------------------------
'''
# 获取当前文件的父目录文件夹
ATM_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(ATM_DIR + "/db/user.text", 'r', encoding='UTF-8') as userFile:
    content = userFile.read()
    global userDic
    userDic = json.loads(content)


login_info = login.login(userDic)
login_status = login_info["status"]
username = login_info["username"]

if login_status is True:
    while True:
        print(mainUI)

        operNum = input("选择操作项：")
        if operNum == str(1):
            transaction.save(userDic,username)

        elif operNum == str(2):
            transaction.withdraw(userDic,username)

        elif operNum == str(3):
            transaction.transfer(userDic, username)

        elif operNum == "exist":
            break

        else:
            print("\033[31;1m没有该选项\033[0m")

        tools.write_dict_into_file(ATM_DIR + "/db/user.text",userDic)