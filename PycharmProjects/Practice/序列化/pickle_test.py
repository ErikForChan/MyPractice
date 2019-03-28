# 与JSON不同的是pickle不是用于多种语言间的数据传输，它仅作为python对象的持久化或者python程序间进行互相传输对象的方法，
# 因此它支持了python所有的数据类型。pickle反序列化后的对象与原对象是等值的副本对象，类似与deepcopy。
from datetime import date
import pickle
import json
list = [1,2,3]
src_dic = {"date":date.today(), "oth":"123"}
# print(src_dic)
# data = pickle.dumps(src_dic)
# print(type(src_dic))
with open("pickle.txt", "w", encoding='UTF-8') as f:
    f.write(pickle.dumps(src_dic))
    # pickle.dump(list,f)
