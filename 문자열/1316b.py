T = int(input())

sum = 0
err = 0
for i in range(T):
    word = input()
    for ii in range(len(word)-1):
        if word[ii] != word[ii+1]:
            if word.count(word[ii]) > 1:
                err += 1
            else:
                pass
        else:
            sum +=1

print(sum)