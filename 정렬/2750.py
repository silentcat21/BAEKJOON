import sys

N = int(sys.stdin.readline())
number = []

for i in range(N):
    number.append(int(sys.stdin.readline()))

number = sorted(number)

for i in range(len(number)):
    print(number[i])

