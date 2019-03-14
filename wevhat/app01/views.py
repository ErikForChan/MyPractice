#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/3/11 15:48
# software: PyCharm
import requests
import time
import re


def login(request):
    if request.method == 'GET':
        cur_time = int(time.time() * 1000)
        base_uuid_url = "https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=en_US&_={0}"
        url = base_uuid_url.format(cur_time)
        r1 = requests.get(url)
        print(r1.text)
        result = re.findall('= "(.*)";')
        id = result[0]
        # 存储session:cur_time,
        return render(request,'login.html',{'id':id})


def check_login():
    cur_time = int(time.time() * 1000)
    base_uuid_url = "https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=en_US&_={0}"
    requests.get()
