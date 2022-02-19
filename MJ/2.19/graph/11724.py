# 12:27-> 12:57
# 12:57[Success]
from collections import deque
import sys
sys_input = sys.stdin.readline
N, M = map(int, input().split())
if M == 0:
    print(0)
    exit(0)
graph = [[]*1 for _ in range(N+1)]
visited = [False] * (N+1)
cnt_component = 0

for _ in range(M):
    a, b = map(int, sys_input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    if visited[i]:
        continue
    cnt_component += 1
    queue = deque([i])

    while queue:
        now = queue.popleft()
        if visited[now]:
            continue
        visited[now] = True
        for to in graph[now]:
            if not visited[to]:
                queue.append(to)
print(cnt_component)
