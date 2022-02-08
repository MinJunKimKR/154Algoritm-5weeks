# 11724. 연결 요소의 개수

import sys
sys.setrecursionlimit(10000) # Python 재귀 제한

def dfs(n):
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)] # 0 ~ n 정점의 개수만큼
visited = [False] * (n + 1)

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

linkCnt = 0     # 연결 요소의 개수
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        linkCnt += 1

print(linkCnt)
