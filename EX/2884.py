H, M = map(int, input().split())

if M < 45 and H > 0:
    H = H - 1
    M = 60 + (M - 45)
    print(H, M)
elif M < 45 and H == 0:
    H = 23
    M = 60 + (M - 45)
    print(H, M)
else:
    H = H
    M = M - 45
    print(H, M)