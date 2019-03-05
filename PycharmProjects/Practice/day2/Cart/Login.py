
import json


def user_login():
    file_content = ''
    with open("user_db.txt",'r',encoding='UTF-8') as file:
        file_content = file.read()
    print(file_content)
    user_dict_db = json.loads(file_content)  # 将文件中的内容序列化为字典，用户信息数据库，用字典方式存储 姓名:[密码:尝试登陆次数]
    # 当某个用户登陆失败三次，则锁定该用户并退出
    while(True):
        print("-----------请输入用户名和密码进行登录------------")
        name = input("姓名：")
        pwd = input("密码：")
        if name in user_dict_db:
            print(user_dict_db[name][0])
            if user_dict_db[name][1] == 3:
                print("你的曾经连续输入错误超过三次！账户已被锁定！")
                break;
            else:
                if user_dict_db[name][0] == int(pwd):
                    if user_dict_db[name][1] !=0 :
                        user_dict_db[name][1] = 0  # 登陆成功后，尝试登陆次数设为0
                        json.dump(user_dict_db, open('user_db.txt', 'w'))
                    print(name + "，您已成功登录！")
                    break  # 登陆成功后退出循环，进入下一个功能
                else:
                    user_dict_db[name][1] += 1  # 密码错误后，尝试登陆次数加1
                    print("密码错误")
                    print(user_dict_db)
                    json.dump(user_dict_db,open('user_db.txt','w'))
                    if user_dict_db[name][1] == 3:
                        print("你的密码输入错误超过三次！账户已被锁定！")
                        break;
        else:
            print("该用户不存在")
