#1085 직사각형에서 탈출

import sys

x, y, w, h = map(int, sys.stdin.readline().split())

resX = 0
resY = 0
res = 0

if x < w - x: resX = x
else : resX = w - x

if y < h - y: resY = y
else: resY = h - y

if resX < resY: res = resX
else: res = resY

print(res)
    
