import sys

N = int(sys.stdin.readline())

xylist = []

for i in range(N):
    X, Y = map(int, sys.stdin.readline().split())
    xylist.append([Y,X])

xylist.sort()

for i in xylist:
    print(i[1], i[0])