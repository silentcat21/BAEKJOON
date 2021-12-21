import sys

def Primeb(n):
    if n == 1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    
    return True

while 1:
    add = 0
    T = int(sys.stdin.readline())

    if T == 0:
        break

    for i in range(T+1, 2*T+1):
        if Primeb(i) == True:
            add += 1
    
    print(add)