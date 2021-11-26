import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

D = A*B*C
number = list(str(D))

for i in range(10):
    print(number.count(str(i)))
