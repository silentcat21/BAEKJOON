M = int(input())
N = int(input())

num = [i for i in range(M, N+1)]

sum = 0
max = []

for i in range(N-M+1):
    sosu = 0
    for ii in range(2,num[i]//2+1):
        
        if num[i] % ii == 0:
            sosu += 1
    if sosu == 0:
        max.append(num[i])
        sum += num[i]
    


if sum == 0 :
    print(-1)
elif M == 1 and N == 1:
    print(-1)
elif M == 1:
    print(sum -1)
    print(num[1])
else:
    print(sum)
    print(min(max))