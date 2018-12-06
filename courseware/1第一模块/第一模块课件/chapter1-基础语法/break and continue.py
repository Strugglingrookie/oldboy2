#_*_coding:utf-8_*_



count = 0
while count <= 100:
    print("loop ", count)
    if count == 5:
        continue
    count += 1

print('---out of the loop ---')