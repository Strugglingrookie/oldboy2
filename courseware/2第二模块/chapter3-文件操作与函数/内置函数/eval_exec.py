#_*_coding:utf-8_*_


source_code = '''
import time

def test_func():
    for n in (100000, 200000, 300000, 400000):
    #for n in (100,200,300):
        data = b'x'*n
    
        start = time.time()
        b = data
        #print(data)
        while b:
            b = b[1:]
            #print(b)
        print('bytes', n, time.time()-start)
    return '124'


test_func()
'''


# res = exec(source_code)
# print('res',res)

# res = eval('1+1')
# print('res',res)


# eval and exec have these two differences:
#
# 1. eval accepts only a single expression, exec can take a code block that has Python statements: loops, try: except:, class and function/method definitions and so on.
#
# 2. An expression in Python is whatever you can have as the value in a variable assignment:
# a_variable = (anything that you can put into these parentheses is an expression)
# eval returns the value of the given expression, whereas exec ignores the return value from its code, and always returns None (in Python 2 it is a statement and cannot be used as an expression, so it really does not return anything).




code = '''

def foo():
    print ('run foo',sdf)
    return 1234


foo()
'''



c = compile(source=code ,filename='err.txt',mode='exec')

print(c)
exec(c)