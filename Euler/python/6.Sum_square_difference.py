import time
be = time.time()

total = 0
count = 0
for i in range(1,101):
    total += i**2
    count += i
print(count**2-total)

print("use time {0:.10f} s".format(time.time()-be))