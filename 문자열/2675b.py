T = int(input())

for i in range(T):
    N, AA = input().split()
    N = int(N)
    AA = list(str(AA))
    for i in range(len(AA)):
        print(N*AA[i], end="")
    print()
    