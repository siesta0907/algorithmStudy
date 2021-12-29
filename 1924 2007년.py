# 1924번 2007년
# x월 y일, 1월1일은 월요일

x, y = map (int, input().split())
day = 0

if x > 1:
    for i in range(1, x):
        if i == 4 or i == 6 or i == 9 or i == 11:
            day += 30
        elif i == 2:
            day += 28
        else:
            day += 31
day += y

if day%7 == 1: print("MON")
elif day%7 == 2: print("TUE")
elif day%7 == 3: print("WED")
elif day%7 == 4: print("THU")
elif day%7 == 5: print("FRI")
elif day%7 == 6: print("SAT")
elif day%7 == 0: print("SUN")
