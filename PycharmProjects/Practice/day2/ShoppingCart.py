
moeny = input("请输入您拥有的金额： ")
# goods列表用户存储所有的商品
goods =[
    ["HuaWei Mate 2",5888],
    ["Xiaomi 8",3888],
    ["Iphone XR",6777],
    ["Smartisan 2",2888],
    ["OPPO R11",3799],
]
if moeny.isdigit(): # 如果输入的数据是一个数字
    moeny = int(moeny)
    lists = '---------------商品列表----------------\n'

    for index,item in enumerate(goods): # 列举出列表的数据
        lists += "No.%d, %s, ￥%d" %(index,item[0],item[1]) + "\n"

    print(lists)

    cart = []
    num = input("请输入要购买的商品编号（按回车即购买，输入 exit 退出）：")
    while num != 'exit':
        if num.isdigit():
            if(int(num) < len(goods)):
                item = goods[int(num)]
                if moeny >= item[1]:
                    cart.append(item)
                    moeny -= item[1]
                    print("您已购买[" + item[0] + "]，价值[￥" + str(item[1]) + "]，您的余额：￥" + str(moeny))
                else:
                    print("余额不足...请选择请他商品")
            else:
                print("商品编号不存在")
        else:
            print("您输入的编号好像不对哦...")
        num = input("请输入要购买的商品编号（按回车即购买，输入 exit 退出）：")

    conclusion = "--------------购物车列表-------------\n"
    for index,item in enumerate(cart):
        conclusion += "No.%d, %s, ￥%d" %(index,item[0],item[1]) + "\n"
    conclusion += "余额: "+str(moeny)
    print(conclusion)

else:
    print("您输入的金额好像不对哦...")
