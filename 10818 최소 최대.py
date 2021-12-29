#10818 최소, 최대

import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

M = nums[0]
m = nums[0]

for num in nums:
    if M < num: M = num
    if m > num: m = num

print(m, M)
