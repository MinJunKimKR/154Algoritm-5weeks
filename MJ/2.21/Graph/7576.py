# 7:00 -> 7:30
# 7:33[Time- out]
# refer : https://jae04099.tistory.com/233
# 문제에서 '최소일수', '주변의 토마토들을 익힘' 이라는 말을 봐서 bfs 문제임을 알았다.
# dfs를 쓰면 안되는 문제였다. 깊이 들어갈 일이 없기 때문이다.
import sys
from collections import deque
sys.setrecursionlimit(5*1000*1000)
sys_input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
days = 1
vector = [[1, 0], [-1, 0], [0, 1], [0, -1]]
cnt_raw_tomato = 0

queue = deque([])


for _ in range(M):
    row = list(map(int, sys_input().strip().split()))
    cnt_raw_tomato += row.count(0)
    graph.append(row)


for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            queue.append((i, j))
while queue:
    x, y = queue.popleft()
    for vec in vector:
        nx = x + vec[0]
        ny = y + vec[1]
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y]+1
            days = max(days, graph[x][y]+1)
            cnt_raw_tomato -= 1
            queue.append([nx, ny])

if cnt_raw_tomato > 0:
    print(-1)
    exit(0)
print(days-1)
