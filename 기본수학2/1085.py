import sys

x, y, w, h = map(int, sys.stdin.readline().split())

a = w -x
b = h -y

llist = [a, b, x, y]
print(min(llist))