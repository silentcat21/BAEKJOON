num = list((input().split()))

rever = []
for i in range(len(num)):
    rever.append(''.join(reversed(num[i])))

print(max(rever))
