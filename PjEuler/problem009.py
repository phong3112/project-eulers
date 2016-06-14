#coding: utf-8

from math import sqrt
import time
start = time.time()

for b in range(500):
    for a in range(b):
        c = sqrt(a*a + b*b)
        if a + b + c == 1000:
            print a*b*c
            break
print time.time() - start
