#_*_coding:utf-8_*_



s = "Hello world!"
s2 = "Hello world!33333rgddgg"

def get_len(data):
    count = 0
    for i in data:
        count += 1
    print(count)

print(len(s))
get_len(s2)