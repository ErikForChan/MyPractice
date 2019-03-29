#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/17 17:44
# software: PyCharm

import pymysql

conn = pymysql.connect(host='192.168.0.196',user='root',passwd='123456',db='mydatabase')
cur = conn.cursor()
reCount = cur.execute("select * from class")
conn.commit()
data = cur.fetchall()
for d in data:
    print(d)
cur.close()
conn.close()