import time
be = time.time()

num = 1000
to = 0

for i in range(num):
    if i%3==0 or i%5==0:
        to += i
print(to)

print("use time {0:.10f} s".format(time.time()-be))