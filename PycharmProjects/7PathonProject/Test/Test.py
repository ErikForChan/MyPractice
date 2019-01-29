# assert 1 == 2 ,'1只能等于1'  # 断言某个语句为true，如果不为true，则抛出异常，在断言表达式后添加字符串信息，用来解释断言并更好的知道是哪里出了问题
# def fun():
#     pass # pass是空语句，是为了保持程序结构的完整性。

import re

#  正则表达式
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配