#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/19 19:26
# software: PyCharm
import pymysql

conn = pymysql.connect(
    host="192.168.0.196",
    user="root",
    password="123456",
    database="bookshop",
    charset="utf8"
)
cursor = conn.cursor()
# 执行SQL语句
sql = 'select * from book'
cursor.execute(sql)
ret = cursor.fetchall()
for i in ret:
    print(i)
# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()

