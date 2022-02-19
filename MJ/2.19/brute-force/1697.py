# 4:26 -> 4:56
# 4:54[FAIL]
# 4:55 [retry - bfs]
# 5:17 [success]
from collections import deque
N, K = map(int, input().split())

INF = 100000
visited = [0]*(INF+1)
queue = deque([N])

while queue:
    info = queue.popleft()
    if info == K:
        print(visited[info])
        break
    for next in (info-1, info+1, info*2):
        if 0 <= next <= INF and visited[next] == 0:
            queue.append(next)
            visited[next] = visited[info]+1
