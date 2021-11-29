import sys

sum = 0
alist = []
for i in range(10):
    a = int(sys.stdin.readline())
    b = a%42
    alist.append(b)
print(alist)
setlist = set(alist)

print(len(setlist))
    