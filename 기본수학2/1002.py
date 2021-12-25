import sys

T = int(sys.stdin.readline())

for i in range(T):
    x, y, r, xx, yy, rr = map(int, sys.stdin.readline().split())

    distance = ((x-xx)**2 + (y-yy)**2)**0.5

    if distance == r+rr:
        print('1')
    elif distance > r+rr:
        print('0')
    elif 0 < distance < r+rr:
        print('2')
    elif distance == 0 and r != rr:
        print('0')
    elif distance == 0 and r == rr:
        print('-1')
    elif distance**2 < (r-rr)**2:
        print('0')
    elif distance**2 == (r-rr)**2:
        print('1')
    elif distance**2 > (r-rr)**2:
        print('2')
    
