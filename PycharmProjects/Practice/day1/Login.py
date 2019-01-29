
# 用户原始名称与密码
_username,_password = "Jacky","root123456"
# 判断用户是否登录成功
loginSussess = False

# 循环三次，如果成功则跳出循环
for i in range(3):
    print("-----------请输入用户名和密码进行登录------------")
    name = input("姓名：")
    pwd = input("密码：")
    if name == _username and pwd == _password:
        loginSussess = True
        print("恭喜您！登录成功！")
    else:
        continue

if loginSussess is False:
    print("输入错误超过三次！您的账户已被锁定！")