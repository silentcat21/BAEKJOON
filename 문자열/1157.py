word = str(input().upper)
setword = list(set(word))

countlist = []

for i in setword:
    countlist.append(word.count(i))

print(countlist)