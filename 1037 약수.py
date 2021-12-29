#1037 약수

import sys

n = int(sys.stdin.readline())
aliquot = sys.stdin.readline().split()
aliquot = list(map(int, aliquot))
aliquot.sort()

print(int(aliquot[0])*int(aliquot[-1]))
