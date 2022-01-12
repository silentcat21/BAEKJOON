import sys

N = int(sys.stdin.readline())

people = []

for i in range(N):
    people.append(sys.stdin.readline().split())

print(people)


for i in range(N):
    rank = 1
    for ii in range(N):
        if people[i][0] < people[ii][0] and people[i][1] < people[ii][1]:
            rank = rank + 1
    print(rank, end=" ")
