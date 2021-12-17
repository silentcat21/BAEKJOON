T = int(input())

listt = list(map(int, input().split()))

sum = 0
summ = 0

for i in range(T):

    sosu = 0
    for ii in range(1, listt[i]+1):
        
        if listt[i] % ii == 0:
            sosu += 1
        else:
            pass
    
    if sosu == 2:
        sum += 1

print(sum)
