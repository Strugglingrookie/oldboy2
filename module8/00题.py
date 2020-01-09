i=0 #执行次数
j=300    #最后猴子拿到的桃子数
# x=311    #每次均分后，第一只猴子拿了之后剩下的总数
while i<5:
    x=4*j
    for i in range(5):
        if (x%4!=0):
            break
        else:
            i=i+1
        x=(x/4)*5+1
    j+=1

print(x)