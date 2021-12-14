import sys
A, B, V = map(int, sys.stdin.readline().split())

lenth = 0
day = 1

while lenth < V:
    lenth += A
    if lenth >= V:
        break
    else:
        lenth -= B
    day += 1

print(day)
