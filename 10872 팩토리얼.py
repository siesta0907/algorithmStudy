#10872번 팩토리얼
#재귀함수

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)


N = int(input())
print(factorial(N))

