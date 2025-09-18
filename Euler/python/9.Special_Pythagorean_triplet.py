import time
be = time.time()

for a in range(333):
    for b in range(a+1,500):
        c = 1000-b-a
        if c <= b:
            continue
        if a**2+b**2 == c**2:
            print(a,b,c,a*b*c)

print("use time {0:.10f} s".format(time.time()-be))