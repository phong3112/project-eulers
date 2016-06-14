#coding: utf-8

def ucln(a, b):
    while b:
        r = a % b
        a, b = b, r
    return a
def bcnn(a, b):
    bcnn1 = a * b / ucln(a, b)
    return bcnn1

lists = list(range(2,21))

bcnn1 = bcnn(lists[0], lists[1])

for i in range(2,len(lists)):
    bcnn1 = bcnn(bcnn1, lists[i])

print bcnn1


    
        
