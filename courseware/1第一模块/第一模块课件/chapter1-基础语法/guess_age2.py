#_*_coding:utf-8_*_





count = 0
age = 26

while count < 3:

    user_guess = int(input("your guess:"))
    if user_guess == age :
        print("恭喜你答对了，可以抱得傻姑娘回家！")
        break
    elif user_guess < age :
        print("try bigger")
    else :
        print("try smaller")

    count += 1

    if count == 3:
        choice = input("你个笨蛋，没猜对，还想继续么?(y|Y)")
        if choice == 'y' or choice == 'Y':
            count = 0
