import time
be = time.time()

def palinums(num):
    return "".join(reversed(list(str(num)))) == str(num)

flag = 0
for i in range(100,1000):
    for j in range(100,1000):
        if palinums(i*j):
            if i*j > flag:
                flag = i*j

print(flag)
print("use time {0:.10f} s".format(time.time()-be))