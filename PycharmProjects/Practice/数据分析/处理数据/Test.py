#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/18 16:29
# software: PyCharm

from pandas import read_csv,read_table,read_excel,DataFrame,to_datetime

#导入数据
df = read_csv('E://test.csv',encoding='UTF-8',sep=" ",names=['name','age'])

df = read_table('E://test.txt',encoding='UTF-8')

df = read_excel('E://test.xlsx',sheet_name="data")

#导出数据
df = DataFrame({
    'age':[11,33,66],
    'name':['Jack','Mark','John']
})
df = DataFrame({
    'age':[11,33,66],
    'name':"Dave"
})
df.to_csv('E://test.csv')

#重复值处理
df.drop_duplicates() #返回一个没有重复值的df

#缺失值处理
df.dropna()#除去值为空的数据

df['name'] = df['name'].astype(str)
#除去空格
df['name'].str.strip()

#字段抽取
df['name'].str.slice(0.2)

#字段拆分
df['name'].str.splite()

#随机抽样
import numpy
numpy.random.randint(0,10,2) #0到10之前随机抽取两个数

#记录合并
df1 = DataFrame({
    "age":12,
    "name":"123"
})
df2 = DataFrame({
    "age":12,
    "name":"123"
})
import pandas
df3 = pandas.concat(df1,df2)

#字段合并
df = df.astype(str)
df['name'] + df['age'] #前提是 先要转化曾str

#字段匹配
df3= DataFrame({
    "add":"2321",
    "name":"123"
})
item_name = pandas.merge(df1,df3,left_on="name",right_on="name")

#数据标准化
# scale = (x - min)/(max - min)

#数据分组
bins = [min(df.age)-1,10,20]

labels = ['10一下',"10-20","20以上"]
pandas.cut(df.age,bins,labels=labels)

#日期转换
df_dt = to_datetime(df.time,format="%Y/%m/&d")

from datetime import datetime
#日期格式化
df_dt_str = df_dt.apply(lambda x:datetime.strftime(x,"%d-%m-%Y"))

#日期抽取
df_dt.dt.year
df_dt.dt.day