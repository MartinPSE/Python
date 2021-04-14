from collections import deque
from sys import stdin


def bfs(graph, start):
    queue = deque([start])
    visited = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))

    return visited


N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


print(len(bfs(graph,1))-1)


