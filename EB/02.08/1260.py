# 1260. DFS와 BFS

def dfs(n):
    print(n, end=' ')
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

def bfs(n):
    visited[n] = True
    queue = deque([n])  # deque 객체 생성
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

import sys
from collections import deque
    
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)   # 0 ~ n까지

print(graph)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

dfs(v)
visited = [False] * (n + 1)
print()
bfs(v)

