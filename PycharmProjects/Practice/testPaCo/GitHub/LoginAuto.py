#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/3/1 14:48
# software: PyCharm

import requests
from bs4 import BeautifulSoup

response = requests.get('https://github.com/login')
s1 = BeautifulSoup(response.text,'html.parser')
token = s1.find(name='input',attrs={'name':'authenticity_token'}).get('value')
print(token)

r2 = requests.post(url='https://github.com/session',
                   data={
                        'utf8': '✓',
                        'commit': 'Sign in',
                        'authenticity_token': token,
                        'login': '1043490933@qq.com',
                        'password': 'chenjiaming917'
                   },
                   cookies = response.cookies.get_dict()
                   )

# print(r2.text)
cook_dict = r2.cookies.get_dict()

r3 = requests.get(
    url='https://github.com/settings/emails',
    cookies = cook_dict
)

print(r3.text)