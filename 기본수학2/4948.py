import sys

def Primeb(n):
    primelist =[True]*2*n

    if n == 1:
        primelist.append(2)
    else:
        for i in range(n, n*2+1):
            for ii in range(2, int(i**0.5)+1):
                if i % ii == 0:
                    primelist.remove(primelist[-1])
                    
    
    return print(len(primelist))                
    


while 1:
    T = int(sys.stdin.readline())
    if T == 0:
        break
    Primeb(T)
