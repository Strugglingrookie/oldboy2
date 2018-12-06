#_*_coding:utf-8_*_



score = int(input(">>:"))


if score > 100:
    print("成绩最多只能到100")
elif score >= 90 :
    print("A")

elif score >= 80:
    print("B")

elif score >=60 :
    print("C")

elif score >= 40:
    print("D")
elif score >=0 :
    print("E")
else:
    print("成绩不能是负数")


