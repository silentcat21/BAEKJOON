word = list(input())

number = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
sum = 0

for i in range(len(word)):
    for ii in range(len(number)):
        if word[i] in number[ii]:
            sum += 3+ii
        else:
            pass

print(sum)
