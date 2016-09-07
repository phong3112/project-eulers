# coding: utf-8
c = []
for i in range(999):
    for j in range(999):
        a = i * j
        b = a % 1000
        d = a / 1000
        if (str(d) == str(b)[::-1]):
            c.append(a)
print max(c)
