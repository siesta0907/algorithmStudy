#12865

"""
첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)
두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와
해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

"""
weight = []
value = []
N, K = map(int,input().split())
for n in range(N):
    W, V = map(int,input().split())
    weight.append(W)
    value.append(V)

maxValue = 0

for i in range(N):
    for j in range(N):
        if i == j:
            if weight[i] <= K and maxValue < value[i]:
                maxValue = value[i]
        elif weight[i] + weight[j] <= K and maxValue < value[i] + value[j]:
            maxValue = value[i] + value[j]
print(maxValue)
