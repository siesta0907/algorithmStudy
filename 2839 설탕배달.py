# 2839 설탕배달
# 5키로 설탕 3키로 설탕

n = int(input())
x = 0
for i in range(0, n//3+1):
    if (n - 3*i) % 5 == 0:
        j = (n - 3*i)//5
        x = 1
        print(i+j)
        break
if x == 0:
    print(-1)
