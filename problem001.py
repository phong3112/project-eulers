# coding: utf-8
s = 0
for i in range(1000):
    #print i,
    if (i % 3 == 0):
        s = s + i
    if (i % 5 == 0):
        s = s + i
    if (i % 15 == 0):
        s = s - i
print s
