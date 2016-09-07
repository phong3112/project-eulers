#coding: utf-8

c = [1]
a,b = 1,2
s = 0
while b <4000000:
    a,b = b, a+b
    c.append(a)
print c
print len(c)
for i in range(len(c)):
    if c[i] % 2 == 0:
        s = s + c[i]
print s
    
    
