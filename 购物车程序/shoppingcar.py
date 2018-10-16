# """购物车程序"""
products = [['iphone8', 6888], ['MacPro', 14800], ['小米8', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]
exit_flag = False
mon_salary = input("please input your monthly salary:")
balance = int(mon_salary)
shop_car = []
while not exit_flag:
    print("commodity lies".center(20, '-'))
    for index, p in enumerate(products):
        print("%s. %s     %s" % (index, p[0], p[1]))
    choice_commodity = input("please input commodity number which you want:")
    if choice_commodity == 'q':
        print("this commodity you have buy:".center(30, "-"))
        for index, p in enumerate(shop_car):
            print("%s. %s     %s" % (index, p[0], p[1]))
        print("cost total: %s   remaining money: %s" % (int(mon_salary)-balance, balance))
        exit_flag = True
    elif 0 <= int(choice_commodity) <= 5:
        choice_commodity = int(choice_commodity)
        if products[choice_commodity][1] <= balance:
            shop_car.append(products[choice_commodity])
            balance -= products[choice_commodity][1]
        else:
            print("you don't have enough money,please choose other commodity.")
    else:
        print("input illegal")


# 运行示例
# please input your monthly salary:10000
# ---commodity lies---
# 0. iphone8     6888
# 1. MacPro     14800
# 2. 小米8     2499
# 3. Coffee     31
# 4. Book     80
# 5. Nike Shoes     799
# please input commodity number which you want:0
# ---commodity lies---
# 0. iphone8     6888
# 1. MacPro     14800
# 2. 小米8     2499
# 3. Coffee     31
# 4. Book     80
# 5. Nike Shoes     799
# please input commodity number which you want:5
# ---commodity lies---
# 0. iphone8     6888
# 1. MacPro     14800
# 2. 小米8     2499
# 3. Coffee     31
# 4. Book     80
# 5. Nike Shoes     799
# please input commodity number which you want:1
# you don't have enough money,please choose other commodity.
# ---commodity lies---
# 0. iphone8     6888
# 1. MacPro     14800
# 2. 小米8     2499
# 3. Coffee     31
# 4. Book     80
# 5. Nike Shoes     799
# please input commodity number which you want:q
# -this commodity you have buy:-
# 0. iphone8     6888
# 1. Nike Shoes     799
# cost total: 7687   remaining money: 2313
#
# Process finished with exit code 0
