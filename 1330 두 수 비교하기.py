#1330번 두 수 비교하기

a = input()

nums = a.split()

A = int(nums[0])

B = int(nums[1])

if A > B:
    print(">")
elif A < B:
    print("<")
elif A == B:
    print("==")
