import time
be = time.time()

def odd_iter():
    n = 1
    while True:
        n = n+2
        yield n

def not_divisible(n):
    return lambda x: x%n > 0

def primes():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n),it)

total = 600851475143
prime = []
for i in primes():
    if total == 1:
        break
    while total%i == 0:
        total = total/i
        prime.append(i)
        
print(prime[-1])
print("use time {0:.10f} s".format(time.time()-be))