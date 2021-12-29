# 10773번 제로
# stack

stack = []
K = int(input())
res = 0

for i in range (K):
    n = int(input())
    if stack and n == 0:
        stack.pop()
    else:
        stack.append(n)

for i in stack:
    res += i

print(res)
