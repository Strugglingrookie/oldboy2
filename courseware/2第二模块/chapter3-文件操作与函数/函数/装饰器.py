
user_status = False  # 用户登录了就把这个改成True



def login(auth_type):

    def auth(func):
        def inner(*args,**kwargs):
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
            if user_status:
                print("用户已登录，验证通过...",func)

                func(*args,**kwargs)
        return inner
    return auth

def home():
    print("---首页----")


def america():
    print("----欧美专区----")


def japan():
    print("----日韩专区----")


#@login('qq')
def henan(video_type):
    print("----河南专区----",video_type)

henan =  login('qq')(henan)
# america =  login(america)
# henan('3p')
# america()

print(henan)
henan('3p')