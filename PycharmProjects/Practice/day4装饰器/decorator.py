username = 'root'
password = '123456'


import datetime


def count_time(func):
    def wrapper(*args,**kwargs):
        start_time = datetime.datetime.now()
        print(start_time)
        func()
        end_time = datetime.datetime.now()
        print(end_time)
        print(end_time-start_time)
    return wrapper


@count_time
def main():
    print('>>>>开始计算函数运行时间')
    for i in range(1, 100):  # 可以是任意函数  ， 这里故意模拟函数的运行时间
        for j in range(i):
            print(j)

# 用于验证用户信息的装饰器

def auth(type):
    def deco(func):
        def wrapper(*args,**kwargs):
            name = input("请输入用户名:").strip()
            pwd = input("请输入密码：").strip()
            if name == username and pwd == password:
                print("\033[32;1m登录成功!\033[0m")
                return func(*args,**kwargs)
            else:
                print("\033[35;1m用户名或者密码错误!\033[0m")
        return wrapper;
    return deco


# 登录界面
@auth(type="local")
def login():
    print("Welcome to Login")
    return "sucess"


# 主界面
@auth(type="ldap")
def home():
    print("Welcome to home")


# 评论界面
@auth(type="tourist")
def comment():
    print("Welcome to comment")


# login()
main()
