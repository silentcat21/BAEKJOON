import sys

xlist = []
ylist = []

for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    xlist.append(x)
    ylist.append(y)

for i in xlist:
    if xlist.count(i) == 1 :
        minx = i
for i in ylist:
    if ylist.count(i) == 1 :
        miny = i

print(minx, miny)