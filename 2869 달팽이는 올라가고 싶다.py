#2869 달팽이는 올라가고 싶다

import sys
import math
a, b, v = map(int, sys.stdin.readline().split())
days = (v - a) / (a - b) + 1
print(math.ceil(days))
