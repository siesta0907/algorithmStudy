# 2750번 수 정렬하기1
# 버블 정렬

N = int(input())
nums = []
res = []
for i in range (0 , N):
    s = input()
    nums.append(int(s))

while nums:
    x = nums[0] 
    for i in range (len(nums)-1):
        if nums[i] > nums[i+1]:
            x = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = x
        else:
            x = nums[i+1]
    
    res.append(x)
    nums.remove(x)


while res:
    print(res.pop())
