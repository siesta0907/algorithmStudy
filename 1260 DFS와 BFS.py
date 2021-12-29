#1260 DFS와 BFS

def DFS (graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph.keys():
                stack.extend(reversed(graph[n]))
    return visited

def BFS (graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n in graph.keys():
                queue.extend(graph[n])
    return visited


graph = {}

N,M,V = map (int, input().split())

for i in range(M):
    n1, n2 = map (int, input().split())
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

for i in graph.keys():
    graph[i] = sorted(graph[i])


res_dfs = DFS(graph,V)
res_bfs = BFS(graph,V)

for i in res_dfs:
    print (i, end = ' ' )
print(end = "\n")
for i in res_bfs:
    print (i, end = ' ' )
