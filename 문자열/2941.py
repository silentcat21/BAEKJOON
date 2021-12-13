word = str(input())

cro = ['c=','c-','dz=','d-','lj','s=','nj','z=']

num = 0

for i in range(len(cro)):   
    if cro[i] in word:
        num -= 1
    else:
        pass
if cro[2] in word:
    num -= 1

num += len(word)

print(num)



