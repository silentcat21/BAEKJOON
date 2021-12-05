S = input()

al = 'abcdefghijklmnopqrstuvwxyz'

for i in al:
    if i in S:
        print(S.index(i), end= ' ')
    else:
        print(-1, end = ' ')

