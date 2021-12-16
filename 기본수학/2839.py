N = int(input())

sugar = 0

while N >= 0:
    if N % 5 == 0:
        sugar += (N//5)
        print(sugar)
        break
    N -= 3
    sugar += 1

else:
    print(-1)
