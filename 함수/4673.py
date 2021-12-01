def self_number(n):
    listn = list(n)
    sum = 0
    for i in listn:
        sum = n + int(i)

    print(sum)


self_number(input())
