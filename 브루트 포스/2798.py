import sys

N, M = map(int, sys.stdin.readline().split())
cardlist = list(map(int, sys.stdin.readline().split()))
sum = 0

for i in range(0, N-2):
    for ii in range(i+1, N-1):
        for iii in range(ii+1, N):
            if cardlist[i] + cardlist[ii] + cardlist[iii] > M:
                continue
            else:
                sum = max(sum, cardlist[i] + cardlist[ii] + cardlist[iii])

print(sum)


    

