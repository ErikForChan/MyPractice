#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/2/27 16:45
# software: PyCharm

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{},
            }
        },
        '闸北':{
            '火车站':{
                '携程':{},
            }
        },
        '浦东':{},
    },
    '山东':{},
}

choice = 'TEST'
cur_menu = menu
temp_menus = []
while choice != 'Q' and choice != 'q':
    menu_list = list(cur_menu.keys())
    if (choice == 'B' or choice == 'b') and cur_menu != menu:
        cur_menu = temp_menus.pop()
    if choice.isdigit():
        key_choosed = menu_list[int(choice)]
        temp_menus.append(cur_menu)
        cur_menu = cur_menu[key_choosed]
    for index,v in enumerate(cur_menu):
        print(index,v)
    choice = input("请选择进入[B返回上一层，Q退出] >>>")

