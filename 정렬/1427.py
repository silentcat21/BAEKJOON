import sys

inputnumber = list(sys.stdin.readline())
del inputnumber[-1]

numberlist =  []

for i in range(len(inputnumber)):
    numberlist.append(int(inputnumber[i]))

numberlist.sort(reverse=True)

for i in range(len(numberlist)):
    print(numberlist[i], end='')