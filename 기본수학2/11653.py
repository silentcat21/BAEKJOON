N = int(input())
soin = 2
while  1:
    if N % soin == 0:
        print(soin)
        N = N/soin
    else:
        soin += 1
    
    if N == 1:
        break