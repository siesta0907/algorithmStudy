import sys


N = int(sys.stdin.readline())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))
    nums.sort()
    length = len(nums)
    if length  %2 == 0:
        print(min(nums[length//2], nums[length//2-1]))
    else:
        print(nums[length//2])