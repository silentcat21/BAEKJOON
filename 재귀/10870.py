import sys

def Fi(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    
    return Fi(n-2) + Fi(n-1)

print(Fi(int(sys.stdin.readline())))