word = input().upper()
setword = list(set(word))

countlist = []

for i in setword:
    countlist.append(word.count(i))

if countlist.count(max(countlist)) > 1 :
    print("?")
else:
    print(setword[countlist.index(max(countlist))])