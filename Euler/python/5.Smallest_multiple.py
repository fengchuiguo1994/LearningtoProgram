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


mydict = {}
for num in range(2,201):
    prime = {}
    for i in primes():
        if num == 1:
            break
        while num%i == 0:
            num = num/i
            if i not in prime:
                prime[i] = 0
            prime[i] += 1
    for i in prime.keys():
        if i not in mydict:
            mydict[i] = prime[i]
        else:
            if mydict[i] < prime[i]:
                mydict[i] = prime[i]
            
total = 1
for i in mydict.keys():
    for j in range(mydict[i]):
        total = total*i

print(total)

print("use time {0:.10f} s".format(time.time()-be))