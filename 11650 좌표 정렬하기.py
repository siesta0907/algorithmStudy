#11650 좌표 정렬하기

N = int(input())
coord = []

for i in range (N):
    x, y = map (int, input().split())
    coord.append([x,y])

coord = sorted(coord)

for i in range (N):
    print(coord[i][0], coord[i][1])
