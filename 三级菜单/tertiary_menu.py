# """三级菜单程序"""
menu = {'安徽省': {'合肥市': ['肥西县', '肥东县', '肥北县'],
                '阜阳市': ['颍上县', '阜南县', '阜北县'],
                '安庆市': ['潜山县', '岳西县', '桐城县']},
        '江苏省': {'南京市': ['江宁区', '玄武区', '鼓楼区'],
                '苏州市': ['沧浪区', '平江区', '姑苏区'],
                '无锡市': ['新吴区', '惠山区', '锡山区']},
        '浙江省': {'杭州市': ['西湖区', '萧山区', '江干区'],
                '宁波市': ['江东区', '镇海区', '北仑区'],
                '温州市': ['龙湾区', '平阳县', '文成县']}}
exit_flag = False
while not exit_flag:
    print("省".center(20, '-'))
    for index, k in enumerate(menu.keys()):
        print("%s . %s" % (index, k))
    choice = input("选择您所在的省(r:返回 ；q:退出)：")
    if choice == 'q':
        print("您已退出")
        exit_flag = True
    elif choice == 'r':
        print("已经是最顶层了")
    elif not choice.isdigit():
        print("输入非法")
    elif choice.isdigit() and int(choice) > len(menu.keys())-1:
        print("您选择的省份不存在")
    elif choice.isdigit() and 0 <= int(choice) <= len(menu.keys())-1:
        addr1 = list(menu.keys())[int(choice)]
        while not exit_flag:
            menu2 = menu[list(menu.keys())[int(choice)]]
            print("市".center(20, '-'))
            for index, k in enumerate(menu2.keys()):
                print("%s . %s" % (index, k))
            choice2 = input("选择您所在的市(r:返回 ；q:退出)：")
            if choice2 == 'q':
                print("您已退出")
                exit_flag = True
            elif choice2 == 'r':
                print("好的，这是上一层")
                break
            elif not choice2.isdigit():
                print("输入非法")
            elif choice2.isdigit() and int(choice2) > len(menu2.keys()) - 1:
                print("您选择的市不存在")
            elif choice2.isdigit() and 0 <= int(choice2) <= len(menu2.keys()) - 1:
                addr2 = list(menu2.keys())[int(choice2)]
                while not exit_flag:
                    menu3 = menu2[list(menu2.keys())[int(choice2)]]
                    print("区/县".center(20, '-'))
                    for index, k in enumerate(menu3):
                        print("%s . %s" % (index, k))
                    choice3 = input("选择您所在的区/县(r:返回 ；q:退出)：")
                    if choice3 == 'q':
                        print("您已退出")
                        exit_flag = True
                    elif choice3 == 'r':
                        print("好的，这是上一层")
                        break
                    elif not choice3.isdigit():
                        print("输入非法")
                    elif choice3.isdigit() and int(choice3) > len(menu3) - 1:
                        print("您选择的区/县不存在")
                    elif choice3.isdigit() and 0 <= int(choice3) <= len(menu3) - 1:
                        addr3 = menu3[int(choice3)]
                        print("你的地址：" + ' '.join([addr1, addr2, addr3]))
                        exit_flag = True
                        break


# 运行示例
---------省----------
0 . 安徽省
1 . 江苏省
2 . 浙江省
选择您所在的省(r:返回 ；q:退出)：r
已经是最顶层了
---------省----------
0 . 安徽省
1 . 江苏省
2 . 浙江省
选择您所在的省(r:返回 ；q:退出)：q
您已退出

Process finished with exit code 0

---------省----------
0 . 安徽省
1 . 江苏省
2 . 浙江省
选择您所在的省(r:返回 ；q:退出)：0
---------市----------
0 . 合肥市
1 . 阜阳市
2 . 安庆市
选择您所在的市(r:返回 ；q:退出)：0
--------区/县---------
0 . 肥西县
1 . 肥东县
2 . 肥北县
选择您所在的区/县(r:返回 ；q:退出)：r
好的，这是上一层
---------市----------
0 . 合肥市
1 . 阜阳市
2 . 安庆市
选择您所在的市(r:返回 ；q:退出)：2
--------区/县---------
0 . 潜山县
1 . 岳西县
2 . 桐城县
选择您所在的区/县(r:返回 ；q:退出)：2
你的地址：安徽省 安庆市 桐城县

Process finished with exit code 0


# # 三级菜单文艺青年版
# menu = {
#     '北京':{
#         '海淀':{
#             '五道口':{
#                 'soho':{},
#                 '网易':{},
#                 'google':{}
#             },
#             '中关村':{
#                 '爱奇艺':{},
#                 '汽车之家':{},
#                 'youku':{},
#             },
#             '上地':{
#                 '百度':{},
#             },
#         },
#         '昌平':{
#             '沙河':{
#                 '老男孩':{},
#                 '北航':{},
#             },
#             '天通苑':{},
#             '回龙观':{},
#         },
#         '朝阳':{},
#         '东城':{},
#     },
#     '上海':{
#         '闵行':{
#             "人民广场":{
#                 '炸鸡店':{}
#             }
#         },
#         '闸北':{
#             '火车战':{
#                 '携程':{}
#             }
#         },
#         '浦东':{},
#     },
#     '山东':{},
# }
#
#
# layers = [menu, ]
# while True:
#     if len(layers) == 0: break
#     current_layer=layers[-1]
#     for key in current_layer:
#         print(key)
#
#     choice=input('>>: ').strip()
#
#     if choice == 'b':
#         layers.pop(-1)
#         continue
#     if choice == 'q':break
#
#     if choice not in current_layer:continue
#
#     layers.append(current_layer[choice])
