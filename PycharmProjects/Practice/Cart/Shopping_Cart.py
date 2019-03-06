#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/3/4 15:04
# software: PyCharm
from sys import path
from Cart import Login
import json

# goods列表用户存储所有的商品
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

def show_goods():
    lists = '---------------商品列表----------------\n'
    for index, item in enumerate(goods):  # 列举出列表的数据
        lists += "%d, %s, ￥%d" % (index, item['name'], item['price']) + "\n"
    print(lists)


def show_cart(cart,moeny):
    cart_list = "--------------购物车列表-------------\n"
    for index, item in enumerate(cart):
        cart_list += "No.%d, %s, ￥%d" % (index, item['name'], item['price']) + "\n"
    cart_list += "余额: " + str(moeny)
    print(cart_list)


def show_record():
    with open("cart_db.txt", 'r', encoding='UTF-8') as file:
        cart_content = file.read()
        cart_db = json.loads(cart_content)
        print("--------------历史购买记录-------------\n")
        record = cart_db[login_name]
        for index, cart_item in enumerate(record):
            print(str(index + 1) + "：", end='')
            for goods_item in cart_item:
                for item in dict(goods_item):
                    # temp = str(goods_item[item]).isdigit()?goods_item[item]:goods_item[item];
                    if item == 'price':
                        print('￥' + str(goods_item[item]), end=' ')
                    else:
                        print(goods_item[item], end=' ')
                print(',', end=' ')
            print('\n')


def save_record(cart):
    with open("cart_db.txt", 'r', encoding='UTF-8') as file:
        cart_content = file.read()
    cart_db = json.loads(cart_content)
    record = cart_db[login_name]
    record.append(cart)
    json.dump(cart_db, open('cart_db.txt', 'w', encoding='utf8'), ensure_ascii=False)


def main():
    if login_status is True:
        cart = []
        moeny = input("请输入您的工资： ")

        if moeny.isdigit():  # 如果输入的数据是一个数字
            moeny = int(moeny)
            show_goods()
            num = input("请输入要购买的商品编号（按Enter即购买，按R查看历史记录，输入 exit 退出）：")
            while num != 'exit':
                if num.isdigit():
                    if (int(num) < len(goods)):
                        item = goods[int(num)]
                        if moeny >= item['price']:
                            cart.append(item)
                            moeny -= item['price']
                            print("您已购买[" + item['name'] + "]，价值[￥" + str(item['price']) + "]，您的余额：￥" + str(moeny))
                        else:
                            print("余额不足...请选择请他商品")
                    else:
                        print("商品编号不存在")
                else:
                    if num.upper() == 'R':
                        show_record()
                    else:
                        print("您输入的编号好像不对哦...")
                num = input("请输入要购买的商品编号（按回车即购买，输入 exit 退出）：")
            show_cart(cart,moeny)
            save_record(cart)
        else:
            print("您输入的金额好像不对哦...")


if __name__ == "__main__":
    login_info = Login.user_login()
    for k, v in login_info.items():
        login_status = v;
        login_name = k;
        break
    main()