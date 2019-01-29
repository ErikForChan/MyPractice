#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2018/12/27 9:29
# software: PyCharm

import os

# 获取当前文件的父目录文件夹
DIR = os.path.dirname(os.path.abspath(__file__))
cwd = os.getcwd()  #获取当前目录即dir目录下
print(cwd)
# 创建添加一个文件
f = open(DIR+"/test.txt","w",encoding='UTF-8')
# 写入文件
str = '''
汉家三十六将军
东方雷动横阵云
鸡鸣函谷客如雾
貌同心异不可数
赤丸夜语飞电光
徼巡司隶眠如羊
当街...
'''
f.write(str)
f.flush()# 强制写入硬盘
f.close()# 关闭文件

# 打开当前文件
with open(DIR+"/poem.txt",'r',encoding='UTF-8') as file:
    # 遍历文件
    for line in file:
        print(line)# 打印文件内容
    print(file.read())
    print(file.readline())# 读取一行
    print(file.readlines())# 读取多行，返回一个列表

# 修改文件
old_str = '将军'
new_str = '帅士'
data = ''
with open(DIR+"/poem.txt",'r',encoding='UTF-8') as file:
    for line in file:
        if old_str in line:
            line = line.replace(old_str,new_str)
        data += line

with open(DIR+"/poem.txt",'w',encoding='UTF-8') as file:
    file.write(data)

# 删除文件内容
f = open(DIR+"/test.txt","w",encoding='UTF-8')
del f

# 删除本地文件
os.remove(DIR+"/test.txt")
