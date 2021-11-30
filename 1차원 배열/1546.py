n = int(input())
test = list(map(int, input().split()))
max = max(test)

mtest = []

for i in test :
    mtest.append(i/max * 100)

testsum = sum(mtest)/n
print(testsum)