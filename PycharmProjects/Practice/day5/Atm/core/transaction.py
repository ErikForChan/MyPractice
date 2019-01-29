#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/21 18:08
# software: PyCharm
from cryptography.hazmat.bindings._openssl import ffi, lib

def save(userDic,username):
    cur_balance = userDic[username]["balance"]
    cur_cash = userDic[username]["cash"]
    saveMoney = input("存入金额:")
    saveNum = int(saveMoney)
    if cur_cash < saveNum:
        print("\033[31;1m现金不足\033[0m")
    else:
        userDic[username]["balance"] = cur_balance + saveNum
        userDic[username]["cash"] = cur_cash - saveNum
        print("\033[32;1m存储成功，余额： [ %s ]\033[0m" % (userDic[username]["balance"]))


def withdraw(userDic,username):
    cur_balance = userDic[username]["balance"]
    cur_cash = userDic[username]["cash"]
    saveMoney = input("取出金额:")
    saveNum = int(saveMoney)
    if cur_balance < saveNum:
        print("\033[31;1m余额不足\033[0m")
    else:
        userDic[username]["cash"] = cur_cash + saveNum
        userDic[username]["balance"] = cur_balance - saveNum
        print("\033[32;1m取钱成功，余额： [ %s ]\033[0m" % (userDic[username]["balance"]))


def transfer(userDic,username):
    accountNum = input("对方账户:")
    transferMoney = input("转账金额:")
    for user in userDic:
        if str(userDic[user]["card"]) == accountNum:
            userDic[user]["balance"] += int(transferMoney)
            userDic[username]["balance"] -= int(transferMoney)
            print("转账成功！您的余额: %s"%userDic[username]["balance"])
            break