import time
be = time.time()

up = 4000000
i = 1
j = 2
total = 2
while j<up:
    i,j = j,i+j
    if j%2 == 0:
        total += j
print(total)
print("use time {0:.10f} s".format(time.time()-be))