# 10814 나이순 정렬

import sys

N = int(sys.stdin.readline())
dic = {}

for i in range (N):
    a, b= sys.stdin.readline().split()
    a = int(a)
    if a in dic:
        dic[a].append(b)
    else:
        dic[a] = [b]
        
Dkey = dic.keys()
Dkey = sorted(Dkey)

for k in range (len(Dkey)):
    for i in dic[Dkey[k]]:
        print(Dkey[k], i)
