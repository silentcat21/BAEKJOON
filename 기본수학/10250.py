T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    column = (N//H)+1
    row = N%H
    if row == 0:
        row = H
        column -= 1
    print(row*100+column)