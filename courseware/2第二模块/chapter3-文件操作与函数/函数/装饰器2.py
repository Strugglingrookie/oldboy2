
user_status = False  # 用户登录了就把这个改成True
def login(func): #henan
    print('login',func)
    def inner(*args,**kwargs): #3p
        _username = "alex"  # 假装这是DB里存的用户信息
        _password = "abc!23"  # 假装这是DB里存的用户信息
        global user_status

        if user_status == False:

            username = input("user:")
            password = input("pasword:")

            if username == _username and password == _password:
                print("welcome login....")
                user_status = True
            else:
                print("wrong username or password!")
        else:
            print("用户已登录，验证通过...")

        if user_status:
            func(*args,*kwargs) #henan()

    return inner

def home():
    print("---首页----")

def america():
    print("----欧美专区----")

@login(japan) #inte
def japan():
    print("----日韩专区----")


@login
def henan(style):
    print("----河南专区----",style)

#
# henan('3p')