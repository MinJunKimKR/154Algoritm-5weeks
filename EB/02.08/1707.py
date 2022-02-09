# 1707. 이분 그래프

def bfs(start):
    visited[start] = True
    queue = deque([start])

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if not visited[i]:
                visited[i] = -visited[a]    # -1 or 1로 표현
                queue.append(i)
            else:
                if visited[i] == visited[a]:
                    return False
    return True

import sys
from collections import deque

k = int(sys.stdin.readline())

for _ in range(k):

    v, e = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    isTrue = True
    
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v+1):
        if not visited[i]:
            if not bfs(i):
                isTrue = False
                break
            
    print("YES" if isTrue else "NO")
