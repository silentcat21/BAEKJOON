T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    apart = [i for i in range(1, n+1)]

    for i in range(k):
        for ii in range(1, n):
            apart[ii] += apart[ii-1]  

    print(apart[-1])