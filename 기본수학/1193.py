#1, 3, 6, 10

X = int(input())

sum = 1
num = 1

while num <=10000000:
    if X <= sum:
        break
    else:
        sum += num + 1
        num += 1
if num % 2 == 1:
    pass
