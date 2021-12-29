#2562 최댓값

import sys

nums = []

for i in range(9):
    num = int(sys.stdin.readline())
    nums.append(num)

M = nums[0]
for i in range(1,9):
    if M < nums[i]: M = nums[i]

print(M)
print(nums.index(M)+1)
