#11651 좌표 정렬하기2

N = int(input())
coord = []

for i in range (N):
    x, y = map (int, input().split())
    coord.append([x,y])

coord = sorted(coord, key=lambda x: (x[1], x[0]))

for i in range (N):
    print(coord[i][0], coord[i][1])
