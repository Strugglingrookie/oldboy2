#_*_coding:utf-8_*_


data = [1, 3, 6, 7, 9, 12, 14, 16, 17, 18, 20, 21, 22, 23, 30, 32, 33, 35]
data = list(range(100000))
print('start to find')
def binary_search(dataset,n):

    mid = int(len(dataset) / 2 )
    if mid > 0 :
        if dataset[mid] > n: # n must in left side
            new_dataset = dataset[:mid]
            print('mid %s is bigger than %s, keep looking in left' %(dataset[mid], n ))
            #print("mid:",mid,dataset[mid],'bigger than ',n,'keep looking in left ',new_dataset)

            binary_search(new_dataset,n)
        elif dataset[mid] < n:     # n must in right  side
            new_dataset = dataset[mid:]
            print('mid %s is smaller than %s, keep looking in right' % (dataset[mid], n))
            #print("mid:", mid,dataset[mid], 'smaller than ', n, 'keep looking in right ',new_dataset)
            binary_search(new_dataset,n)
        else:
            print("find n",dataset[mid])
    else:
        if dataset[0] == n:
            print('finally find n:',dataset[0])
        else:
            print("data %s doesn't exist in dataset "% n )


binary_search(data,122)

print('---done----')