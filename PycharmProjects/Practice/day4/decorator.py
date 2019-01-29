
username = 'root'
password = '123456'


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


login()