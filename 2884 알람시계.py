#2884번 알람시계

a = input()

nums = a.split()

H = int(nums[0])

M = int(nums[1])

if M < 45 and H == 0:
    H = 23
    M = 60 - (45 - M)
    
elif M < 45:
    H = H - 1
    M = 60 - (45 - M)

elif M >= 45:
    M = M -45


print( H , M )
