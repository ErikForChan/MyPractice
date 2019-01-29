#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2018/12/29 9:30
# software: PyCharm

# 人类：一个父类
class human(object):
    nation = "china"

    def __init__(self,name,gender,phone):
        self.name = name
        self.gender = gender
        self.phone = phone

    # 将个人信息存储在列表中,并返回这个列表
    def get_info(self):
        info = []
        info.append(self.name)
        info.append(self.gender)
        info.append(self.phone)
        return info

    def eat(self):
        print("%s is eating",self.name)

    def play(self):
        print("%s is playing", self.name)


# 人类之间的关系
class relation(object):
    def makefriends(self,obj):
        print("%s make friends with %s"%(self.name, obj.name))


# 男人：继承人类的特性
class man(human,relation):
    def __init__(self,name,gender,phone):
        super(man,self).__init__(name,gender,phone)
        print("I'm a man...")

    def work(self):# 子类的方法
        print("%s is working", self.name)

# 女人：继承人类的特性
class woman(human):
    def __init__(self,name,gender,phone):
        super(woman,self).__init__(name,gender,phone)
        print("I'm a woman...")

    def pargent(self):# 子类的方法
        print("%s is pargenting", self.name)

# 定义man和woman的对象
man1 = man("Erik","male","1234567")
woman1 = woman("Flavia","female","2345678")

maninfo = man1.get_info()
womaninfo = woman1.get_info()
print(maninfo)
print(womaninfo)

# man1和woman1交朋友
man1.makefriends(woman1)