#1152번 단어의 개수
# 주어진 문자열 안에 몇 개의 단어가 있는지 세는 프로그램
# 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

a = input()

words = a.split()

print(len(words))
