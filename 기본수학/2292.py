NA = int(input())
sum = 1
n = 1
while n <= 100000:
    
    if NA <= sum :
        break
    else:
        sum += 6*n
        n += 1

print(n)
