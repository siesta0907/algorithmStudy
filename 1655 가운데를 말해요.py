'''

왼쪽 힙은 최대 힙으로 정렬하고, 오른쪽 힙은 최소 힙으로 정렬하면
왼쪽 힙의 첫번째 요소는 항상 중앙값이 된다.
1. 왼쪽 힙과 오른쪽 힙의 길이가 같으면 (요소 * -1) 을 왼쪽 힙에 삽입한다.
2. 그렇지 않으면 오른쪽 힙에 삽입한다.
왼쪽 힙과 오른쪽 힙에 요소가 존재하고, 왼쪽 힙의 (첫번째 요소* -1) 가 오른쪽 첫번째 요소보다 클 때
3. 왼쪽 힙의 첫번째 요소와 오른쪽 힙의 첫번째 요소를 바꿔준다. ( -1을 곱해준 뒤 바꿔준다. )
왼쪽 힙의 (첫번째 요소 * -1)를 출력한다.
'''

import sys
import heapq
input = sys.stdin.readline

n = int(input())
max_h, min_h = [], []

for i in range(n):
    num = int(input())
    if len(max_h) == len(min_h):
        heapq.heappush(max_h, -num)
    else:
        heapq.heappush(min_h, num)

    if len(max_h) >= 1 and len(min_h) >= 1 and max_h[0] * -1 > min_h[0]:
        max_value = heapq.heappop(max_h) * -1
        min_value = heapq.heappop(min_h)
        
        heapq.heappush(max_h, min_value * -1)
        heapq.heappush(min_h, max_value)

    print(max_h[0] * -1)
