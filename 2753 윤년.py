# 2753번 윤년
# 윤년이면 1 아니면 0 출력하는 프로그램
# 4의 배수이면서 100의 배수가 아닌 년도가 윤년이다.
# 100의 배수이면서 400의 배수가 아니면 윤년이 아니다.
# 400의 배수면 윤년이다. (4의배수면서 100의 배수)


num = input()

year = int(num)

if year%400 == 0:
    print(1)
    
elif year%100 == 0:
    print(0)

elif year%4 == 0:
    print(1)

else:
    print(0)
