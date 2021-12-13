word = input()

cro = ['c=','c-','dz=','d-','lj','s=','nj','z=']

for i in cro:
    word = word.replace(i, '0')

print(len(word))