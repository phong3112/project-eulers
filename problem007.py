#coding: utf-8

import time
 
def fast_nth_prime(n, limit = 125000):
      if limit % 2 != 0:
            limit += 1
      primes = [True] * limit
      primes[0],primes[1] = [None, None]
      count = 0
      for ind,val in enumerate(primes):
            if val:
                  primes[ind*2::ind] = [False] * ((limit -1)//ind - 1)
                  count += 1
            if count == n:
                  return ind
      return False
                  
 
start = time.time()
prime = fast_nth_prime(10001)
elapsed = (time.time() - start)
 
print "found %s in %s seconds." % (prime,elapsed)
