import sys

N = int(sys.stdin.readline())

numberlist = [0]*10010

for i in range(N):
    inputnum = int(sys.stdin.readline())
    numberlist[inputnum] = numberlist[inputnum] + 1

for i in range(10010):
    if numberlist[i] != 0:
        for ii in range(numberlist[i]):
            print(i)