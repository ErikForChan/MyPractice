#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/3/19 9:40
# software: PyCharm

new_str = "abccbanmnm23jki"
# print(new_str[2])
# print(new_str[1:6]) #切片，顾首不顾尾
# print(new_str.capitalize()) # 首字母大写
# print(new_str.swapcase()) # 交换字母大小写
# print(new_str.center(30,"*")) #将字符串居中，其余填充为*
# print(new_str.title()) # 首字母大写，字符串非字母元素隔开的每个单词的首字母大写
# new_str.lower()
# new_str.upper()
# print(new_str.find('c',5,6)) #某个字符的索引
# print('_'.join(new_str)) # 将str中的每个字符用_连起来
# msg = '我是{name},爱好{hoppy}'
# print(msg.format(name='Erik',hoppy='girl')) # 格式化
# print(new_str.isalnum()) #字符串是否由字母和数字组成
# print(new_str.isalpha()) #字符串是否由字母组成
# print(new_str.isdigit()) #字符串是否由数字组成
# print(new_str.count('n')) #计算字符个数
# for s in new_str: # 遍历打印
#     print(s)

# 格式化输出
# new_str = '''
#     compunter是%s,cpu是%s
# '''%('电脑','中央控制器')
# new_str = '''
#     compunter是%s,cpu是%s
# '''%('电脑','中央控制器')
new_str = '''
    compunter是{0},cpu是{1}
'''.format('电脑','中央控制器')
print(new_str)