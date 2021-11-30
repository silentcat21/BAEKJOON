C = int(input())

for i in range(C):
    N = list(map(int, input().split()))
    sum = 0
    
    for t in range(N[0]):
        sum += N[t+1]
    avr = sum/N[0]
    abc = 0
    for s in range(N[0]):
        if N[s+1] > avr:
            abc += 1
        else:
            pass
    result = float(100*abc/N[0])
    print(f'{result:.3f}%')
