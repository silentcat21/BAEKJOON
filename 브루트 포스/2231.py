import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    Nn = list(map(int, str(i)))
    M = i + sum(Nn)

    if M == N :
        print(i)
        break
    if i == N:
        print(0)
