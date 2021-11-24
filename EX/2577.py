import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = str(A*B*C)
list_num = list(D)

print(list_num.count(0))