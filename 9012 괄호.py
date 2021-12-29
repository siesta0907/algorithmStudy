# 9012번 괄호

res = []

T = int(input())

for i in range(T):
    stack = []
    string = input()
    
    for s in string:
        if s == '(':
            stack.append(s)
        elif s == ')' and stack:
            stack.pop()
        elif s == ')' and not stack:
            stack.append(s)
            break

    if stack:
        res.append("NO")
    else:
        res.append("YES")
        
for i in res:
    print(i)
