#coding: utf-8

import time
start = time.time()

def prime(limit):
    prime_num = []
    primes = [True] * limit
    primes[0],primes[1] = [None, None]
    for ind,val in enumerate(primes):
        if val:
            primes[ind*2::ind] = [False] * ((limit -1)//ind - 1)
            prime_num.append(ind)
    return prime_num

a = prime(2000000)
s = 0
for i in a:
    s += i
print s, time.time()-start
    
