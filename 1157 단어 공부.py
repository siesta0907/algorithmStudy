#1157 단어 공부
import sys

memo = {}
word = sys.stdin.readline().upper()

for s in word:
    if s in memo:
        memo[s] += 1
    else:
        memo[s] = 1

res = 0
result = ''
overlap = False

for m in memo:
    if m == '\n': break
    if res < memo[m]:
        overlap = False
        res = memo[m]
        result = m
        continue
    elif res == memo[m]:
        overlap = True

if overlap: print("?")
else: print(result)
