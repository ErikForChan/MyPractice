# import random
#
# temp = [i+1 for i in range(35)]
# random.shuffle(temp);
# i = 0
# list = []
# while i < 7:
#  list.append(temp[i])
#  print(temp[i], end="\n")
#  i = i + 1
# list.sort()
#
# print(list[0:6], end="")
#
# print(list[0])

# import random
# import xlrd
# ExcelFile = xlrd.open_workbook(r'test.xlsx')
# sheet = ExcelFile.sheet_by_name('Sheet1')
# i = []
# x = input("请输入具体事件：")
# y = int(input("老师要求的字数："))
# while len(str(i)) < y * 1.2:
#  s = random.randint(1, 60)
#  rows = sheet.row_values(s)
#  i.append(*rows)
# print(" "*8+"检讨书"+" "+"老师：")
# print("我不应该" + str(x)+"，", *i)
# print("再次请老师原谅！")