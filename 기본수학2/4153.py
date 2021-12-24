import sys

while 1:
    xyz = list(map(int, sys.stdin.readline().split()))
    
    if xyz.count(0) >= 1 :
        break
    
    if xyz[0]**2 + xyz[1]**2 + xyz[2]**2 - 2*(max(xyz)**2) == 0:
        print('right')

    else:
        print('wrong')
    

