T = int(input())
sum = 0

for i in range(T):
    word = list(input())
    for ii in word:
        if word.count(ii) == 1 :
            pass
        elif word.count(ii) >= 2:
            if int(ord(word[ii])) == int(ord(word[ii+1])):
                pass
            else:
                break
    sum += 1

print(sum)