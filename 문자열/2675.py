import sys

num, AA = map(str, sys.stdin.readline().split())
AA = list(AA)
for i in range(int(num)):
    print(int(num)*AA[i], end="")