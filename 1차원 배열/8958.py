N = int(input())

for i in range(N):
    pl = list(input())
    sum = 0
    score = 0
    for i in pl:
        if i == 'O':
            score += 1
            sum += score
        else:
            score = 0
    
    print(sum)

