# 15596번 정수 N개의 합
# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수 

def solve(a):
    ans = 0
    for i in a:
        ans = ans + i
    return ans
