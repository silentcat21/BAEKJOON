import sys

M, N = map(int, sys.stdin.readline().split())

box = [i for i in range(M, N+1)]

for ii in box:
    sosu = 0
    for i in range(1, ii+1):
        if ii % i == 0:
            sosu += 1
    if sosu == 2:
        print(ii)