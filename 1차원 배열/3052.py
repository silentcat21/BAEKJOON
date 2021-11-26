import sys

sum = 0
alist = []
for i in range(10):
    a = int(sys.stdin.readline())
    b = a%42
    alist.append(b)
print(alist)
for t in range(10):
    if alist.find(alist[t]) == 1:
        sum += 1

print(sum)
    