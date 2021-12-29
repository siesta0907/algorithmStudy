#2751 수 정렬하기2

import sys

def merge_sorted(arr):
    if len(arr)>1:
        mid  = len(arr)//2
        left = arr [:mid]
        right = arr[mid:]
        l = merge_sorted(left)
        r = merge_sorted(right)
        return merge(l,r)
    else: return arr

def merge (left, right):
    j = 0
    i = 0
    arr = []

    while i< len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    while i < len(left):
        arr.append(left[i])
        i += 1
    while j < len(right):
        arr.append(right[j])
        j += 1
    return arr

N = int(sys.stdin.readline())
nums = []

for n in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)
    
for r in merge_sorted(nums): print(r)


"""
시간초과 개빡치네 쓰벌

import sys

N = int(sys.stdin.readline())
nums = []

for n in range(N):
    num = int(sys.stdin.readline())
    nums.append([num])

while len(nums) > 1:
    for i in range(len(nums)//2):
        new_arr = []

        while len(nums[i]) > 0 and len(nums[i+1]) > 0 :
            if nums[i][0] < nums[i+1][0]:
                new_arr.append(nums[i][0])
                nums[i].pop(0)
            else:
                new_arr.append(nums[i+1][0])
                nums[i+1].pop(0)
        if len(nums[i]) > 0:
            new_arr += nums[i]
            nums.pop(i+1)
            nums.pop(i)
        elif len(nums[i+1]) > 0:
            new_arr += nums[i+1]
            nums.pop(i+1)
            nums.pop(i)
        nums.append(new_arr)   

for r in nums[0]: print(r)
""""

