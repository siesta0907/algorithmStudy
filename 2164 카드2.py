#2164 카드2

import sys

N = int(sys.stdin.readline())

cards = []
for n in range(1, N+1):
    cards.append(n)

t = True
for card in cards:
    if t == True:
        t = False
        continue
    else:
        t = True
        cards.append(card)
print(cards[-1])
