import sys

a = int(sys.stdin.readline())

def han(n):
    hanum = 0
    for i in range(1,n+1):
        if i <= 99:
            hanum += 1
        elif i >= 100:
            t = list(str(i))
            if int(t[0]) - int(t[1]) == int(t[1]) - int(t[2]):
                hanum += 1
    
    return hanum


print(han(a))
            
        

