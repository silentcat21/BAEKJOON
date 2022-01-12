import sys

N = int(sys.stdin.readline())

count = 0
Nnumber = 1

while 1:
    if "666" in str(Nnumber):
        count += 1
    
    if count == N:
        print(Nnumber)
        break

    Nnumber += 1