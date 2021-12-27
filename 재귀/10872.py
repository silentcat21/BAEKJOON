import sys

def factory(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factory(n-1)

print(factory(int(sys.stdin.readline())))