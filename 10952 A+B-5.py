# 10952 A + B - 5

res = []

while True:
    a , b = map(int, input().split())
    if a == 0 and b == 0: break
    else: res.append(a+b)
for r in res: print(r)
