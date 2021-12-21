import sys

m, n = map(int, sys.stdin.readline().split())

def Prime(A):
    if A == 1:
        return False
    
    else:
        for i in range(2, int(A**0.5)+1):
            if A % i == 0:
                return False
        return True

for i in range(m, n+1):
    if Prime(i) == True:
        print(i)    