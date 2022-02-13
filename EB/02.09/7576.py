# 7576. 토마토

from collections import deque

m, n = map(int, input().split())    # 가로, 세로
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()  # 행, 열
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in graph:
    print(i)
    for j in i:
        if j == 0:
            print(-1)
            #exit(0)

    result = max(result, max(i))

print(result - 1)
