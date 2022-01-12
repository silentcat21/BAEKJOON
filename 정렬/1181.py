import sys

N = int(sys.stdin.readline())

wordlist = [[52, 'a']]

for i in range(N):
    word = str(sys.stdin.readline())
    word = word.strip('\n')
    wordlist.append([len(word),word])

wordlist.sort()
print(wordlist)


