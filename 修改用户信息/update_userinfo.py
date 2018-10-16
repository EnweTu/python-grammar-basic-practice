user_f = open('用户信息（utf-8）.txt', 'r', encoding='utf-8')
user_dict = {}
for line in user_f:
    interim_list = line.split(',')
    user_dict[interim_list[0]] = interim_list
# print(user_dict)
count = 3
login_sta = False
login_user = None
option = """
1、打印用户信息
2、修改用户信息
3、修改密码
4、退出
"""
while count > 0:
    user = input("username:")
    pswd = input("password:")
    count -= 1
    for list_in in user_dict.values():
        _user = list_in[0]
        _pswd = list_in[1]
        if user == _user and pswd == _pswd:
            print("welcome %s" % user)
            login_sta = True
            login_user = user
            count = 0
            break
    if login_sta is False:
        print("username or password wrong")
        print("you have %d choice" % count)


def print_info(user):
    user_list = user_dict[user]
    user_info = '''
    --------------------
      1、Name:   %s
      2、Age:    %s
      3、Dept:   %s
      4、Posi:   %s
      5、Phon:   %s
    --------------------
    ''' % (user_list[2], user_list[3],
           user_list[4], user_list[5],
           user_list[6])
    print(user_info)


def change_info(user):
    print_info(user)
    choice2 = input("请选择要修改的选项：")
    if choice2 == '1':
        new_name = input("请输入新Name：")
        if new_name is not None:
            user_dict[user][2] = new_name
        else:
            print("输入非法")
    elif choice2 == '2':
        new_age = input("new age:")
        if new_age is not None:
            user_dict[user][3] = new_age
        else:
            print("输入非法")
    else:
        print("输入非法")
    print_info(user)
    f = open('用户信息（utf-8）.txt', 'r+', encoding='utf-8')
    for lis in user_dict.values():
        line2 = ','.join(lis)
        f.write(line2)
    f.close()


def change_pswd(user):
    old_pswd = input("请输入原密码：")
    if old_pswd == user_dict[user][1]:
        new_pswd1 = input("请输入新密码：")
        if new_pswd1 is not None:
            new_pswd2 = input("请确认新密码:")
            if new_pswd2 is not None and new_pswd2 == new_pswd1:
                user_dict[user][1] = new_pswd1
    f = open('用户信息（utf-8）.txt', 'r+', encoding='utf-8')
    for lis in user_dict.values():
        line2 = ','.join(lis)
        f.write(line2)
    f.close()


while login_sta is True:
    print("功能选项".center(20, '-'))
    print(option)
    choice = input("请选择：")
    if choice == '1':
        print_info(login_user)
    elif choice == '2':
        change_info(login_user)
    elif choice == '3':
        change_pswd(login_user)
    elif choice == '4':
        login_sta = False
