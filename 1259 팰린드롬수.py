# 1259 팰린드롬수

import sys
import math

nums = []
res = []

while True: 
  num = input()
  if num == '0':
      break
  else:
      nums.append(num)

for num in nums:
    if len(num) == 1:
        res.append("yes")
        continue
    for i in range(len(num)):
        if num[i] != num[-i-1]:
            res.append("no")
            break
        if i == math.ceil(len(num)/2):
            res.append("yes")
            break
        
for r in res:
    print(r)
