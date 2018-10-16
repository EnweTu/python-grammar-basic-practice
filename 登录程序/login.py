"""
登录程序
1、用户信息在文件中
2、允许多用户登录
3、3次机会，账户锁定
4、成功显示欢迎
"""


import os
count = 3
login_state = False
while count > 0:
    user = input("username:").strip()
    pswd = input("password:").strip()
    count -= 1
    info = open('登录程序用户信息（utf-8）.txt', 'r', encoding='utf-8')
    info_new = open('登录程序用户信息（utf-8）new.txt', 'w', encoding='utf-8')
    for line in info:
        if user in line:
            if line.startswith('*'):
                print("account locked")
                count = 0
            else:
                user_info = line.split()
                if user == user_info[0] and pswd == user_info[1]:
                    print("welcome %s" % user_info[0])
                    count = 0
                    login_state = True
                else:
                    print("username or password wrong")
                    print("have %d choice" % count)
            if count == 0 and not line.startswith('*') and login_state is False:
                print("wrong 3 times,account will lock")
                line = '*' + line
        info_new.write(line)
    info_new.close()
    info.close()
    os.remove('登录程序用户信息（utf-8）.txt')
    os.rename('登录程序用户信息（utf-8）new.txt', '登录程序用户信息（utf-8）.txt')
    