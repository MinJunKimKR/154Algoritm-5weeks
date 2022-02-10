# 2178. 미로 탐색 - 풀이 보충

import sys

n, m = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

graph[0][0] = 1  # 시작 위치 포함

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = [[0, 0]]  # 시작 좌표

#BFS 시작
while queue:
    x, y = queue[0][0], queue[0][1]
    
    del queue[0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            queue.append([nx, ny])
            graph[nx][ny] = graph[x][y] + 1 # step

            
        
print(graph[n-1][m-1])  # 도착지점 
