def self_number(n):
    sum = 0
    listn = list(str(n))
    for i in listn:
        sum = sum + int(i)
    return sum + int(n)

num = []
for i in range(10001):
    self = self_number(i)
    num.append(self)

for i in range(10001):
    if i in num:
        pass
    else:
        print(i)

