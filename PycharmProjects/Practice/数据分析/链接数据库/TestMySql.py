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


with conn:
    cur=conn.cursor()
    # cur.execute("ALTER TABLE Writers ADD COLUMN Intruction varchar(96) not null")
    # cur.execute("ALTER TABLE Writers CHANGE COLUMN Intruction Description varchar(96) not null")
    # cur.execute("UPDATE Writers set Description='Test'")

    # cur.execute("CREATE TABLE IF NOT EXISTS Writers(Id INT PRIMARY KEY AUTO_INCREMENT,Name VARCHAR(25))")
    # cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
    # cur.execute("INSERT INTO Writers(Name) VALUES('hONORE DE bALZAC')")
    # cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
    # cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
    # cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")

# cursor = conn.cursor()
# # 执行SQL语句
# sql = 'select * from book'
# cursor.execute(sql)
# ret = cursor.fetchall()
# for i in ret:
#     print(i)
# # 关闭光标对象
# cursor.close()
# # 关闭数据库连接
# conn.close()

