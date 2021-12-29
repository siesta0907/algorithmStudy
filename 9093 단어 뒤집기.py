#9093 단어 뒤집기

import sys

T = int(sys.stdin.readline())
res = []

for t in range(T):
    reverseS = []
    sentence = sys.stdin.readline().split()
    for word in sentence:
        reverseS.append(word[::-1])
    res.append(reverseS)

for r in res:
    for i in r:
        print(i, end = ' ')
    print()
