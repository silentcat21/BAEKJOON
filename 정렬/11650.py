import sys

N = int(sys.stdin.readline())

xylist = []

for i in range(N):
    X, Y = map(int, sys.stdin.readline().split())
    xylist.append([X,Y])

xylist.sort()

for i in xylist:
    print(i[0], i[1])