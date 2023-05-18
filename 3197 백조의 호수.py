import sys

input = sys.stdin.readline

def isSwanCanMeet(lake):
    S1 = swan[0]  #출발점
    S2 = swan[1]  #도착점
    # 출발점에서 도착점에 도착할 수 있는지?



    return True

R,C = map(int, input().split())
lake = [['' for col in range(R)] for row in range(C)]
swan = []
day = 1

for i in range(R):
   string = input()
   for j in range(C):
        if string[j] == 'L':
            swan.append((i,j))
        lake[i][j] = string[j]


if isSwanCanMeet(lake):
    print(day)
else:
    for i in range(R):
        for j in range(C):
            if lake[i][j] == '.':
                try:
                    lake[i - 1][j] = '.'
                except:
                    pass
                try:
                    lake[i + 1][j] = '.'
                except:
                    pass
                try:
                    lake[i][j - 1] = '.'
                except:
                    pass
                try:
                    lake[i][j + 1] = '.'
                except:
                    pass