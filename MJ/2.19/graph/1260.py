# 11:02 -> 11:32
# 11:24 [GG]
# 11:50 [Success]
from collections import deque
import sys
sys_input = sys.stdin.readline
N, M, V = map(int, input().split())
graph = [[] * 1 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys_input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, len(graph)):
    graph[i] = sorted(graph[i])
visited = [False] * (N+1)


def dfs(start, visited):
    if visited[start]:
        return
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if visited[i] == False:
            dfs(i, visited)


def bfs(start, visited):
    queue = deque([start])
    while queue:
        now = queue.popleft()
        if visited[now]:
            continue
        visited[now] = True
        print(now, end=' ')
        for i in graph[now]:
            if visited[i] == False:
                queue.append(i)


dfs(V, visited)
print()
visited = [False] * (N+1)
bfs(V, visited)
