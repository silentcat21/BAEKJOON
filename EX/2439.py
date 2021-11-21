N = int(input())

for i in range(N):
    star = str("*"*(i+1))
    print(star.rjust(N))
