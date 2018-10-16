"""
深度搜索
1、打印所有的节点
2、输入一个节点名字，沙河，遍历找，找到打印并返回True

"""
menus = [
    {
        'text': '北京',
        'children': [
            {'text': '朝阳', 'children': []},
            {'text': '昌平', 'children': [
                {'text': '沙河', 'children': []},
                {'text': '回龙观', 'children': []}
            ]},
        ]
    },
    {
        'text': '上海',
        'children': [
            {'text': '宝山', 'children': []},
            {'text': '金山', 'children': []},
        ]
    }
]


# # 第一个要求
def text_print(menu):
    if len(menu) != 0:
        for i in menu:
            print(i['text'])
            text_print(i['children'])


text_print(menus)


# 第二个要求
def text_find(menu, text_f):
    if menu:
        for i in menu:
            if i['text'] == text_f:
                print(i['text'])
                return True
            res = text_find(i['children'], text_f)
            if res is True:
                break
        return res


text_find(menus, '沙河')
