import re
# s = input()
#
# k = re.search(r'-?[\d\.]+[*/]-?[\d\.]+', s).group()
# print(k)

# re.match #从开始位置开始匹配，如果开头没有则无
# re.search #搜索整个字符串
# re.findall #搜索整个字符串，返回一个list
# re.search 扫描整个字符串并返回第一个成功的匹配。 r(raw)用在pattern之前，表示单引号中的字符串为原生字符，不会进行任何转义
re.match(r'l','liuyan1').group()  #返回l
re.match(r'y','liuyan1')  #返回None

re.search(r'y','liuyan1').group() #返回y

# re.I	使匹配对大小写不敏感
# re.L	做本地化识别（locale-aware）匹配
# re.M	多行匹配，影响 ^ 和 $
# re.S	使 . 匹配包括换行在内的所有字符
# re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
str = re.search(r'[a-z]+','liuyaN1234ab9',re.I).group()
print(str)

rr=re.match(r'[0-9]','325')
g1 = rr.group(0)
print(rr)

#[...] 匹配任意一个字符
#无捕获组 ‘(?: )’
s = 'I have a dog , I have a cat'
re.findall( r'I have a (?:dog|cat)' , s ) # ['I have a dog', 'I have a cat']

# /d 数字  /D 非数字  /w 字母和数字 /W 非字母和数字  /s 间隔符  /S非间隔符
