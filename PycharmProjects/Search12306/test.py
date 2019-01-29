import getpass

name = input("name_: ")
# name = getpass.getpass()
info = '''
name:%s
''' %(name)

# 格式化实现
info2 = '''
name2:{_name}
'''.format(_name=name)

# 用格式化索引实现
info3 = '''
name3:{0}
'''.format(name)

if name == 'wqwwq':
    print(info)
    print(info2)
    print(info3)
else:
    print("error")
