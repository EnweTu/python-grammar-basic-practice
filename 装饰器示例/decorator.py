login_state = False


def login(auth_type):
    def outer(func):
        def inner(*args, **kwargs):
            global login_state
            _user = 'alex'
            _pawd = '1234'
            if login_state is False:
                user = input("username:")
                pawd = input("password:")
                if user == _user and pawd == _pawd:
                    print("welcome %s" % user)
                    login_state = True
                else:
                    print("username or password is wrong")
            else:
                print("you pass")
            if login_state is True:
                func(*args, **kwargs)
        return inner
    return outer


def home():
    print('首页'.center(10, '-'))


@login('qq')    #  japan = login(japan)
def japan(style):
    print('日韩'.center(10, '-'), style)


@login('qq')     #  american = login(american)
def american():
    print('欧美'.center(10, '-'))


def china():
    print('国产'.center(10, '-'))


japan('3p')
american()
