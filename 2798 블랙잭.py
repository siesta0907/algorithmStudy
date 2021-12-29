#2798 블랙잭
import sys

N, M = map(int,sys.stdin.readline().split())
cards = sys.stdin.readline().split()
cards = list(map(int, cards))
cards.sort()

