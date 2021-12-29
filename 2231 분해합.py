#2231 분해합

memo = {}

for i in range (1000):
    m = i + i //1000 + i//100 + i//10 + i%10
    if m in memo: memo[m].append(i)
    else: memo[m] = [i]
    
print(memo)
