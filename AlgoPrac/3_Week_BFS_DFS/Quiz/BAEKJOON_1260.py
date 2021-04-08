from sys import stdin
from collections import deque


def dfs(graph, start):
    stack = [start]
    visited = []
    while stack:
        node = stack.pop()
        print("DFS 결과 값 ",visited, "검사하는 값" ,node)

        if node not in visited:
            visited.append(node)
            stack.extend(sorted(graph[node], reverse=True))

    return visited


def bfs(graph, start):
    queue = deque([start])
    visited = []
    while queue:
        node = queue.popleft()
        print("BFS 결과 값 ",visited, "검사하는 값" ,node)
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))

    return visited


N, M, V = map(int, stdin.readline().split())

# 이 문제에서만 특별히 하나의 graph로 BFS / DFS 다 점검하기 때문에 set 함수를 사용해주는 함정


graph = [set([]) for _ in range(N + 1)]

# graph 모양 만드는거 [ [] ] 생각하기!

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)


print("BFS result",bfs(graph, V))
print("DFS result",dfs(graph, V))
