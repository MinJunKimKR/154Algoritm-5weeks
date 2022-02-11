# 2146. 다리 만들기 - 풀이 참고

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 섬을 구분해주는 bfs
def bfs1(i, j):
    global count
    q = deque()
    q.append([i, j])
    vis[i][j] = True
    arr[i][j] = count

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and not vis[nx][ny]:
                vis[nx][ny] = True
                arr[nx][ny] = count
                q.append([nx, ny])

# 바다를 건너며 가장 짧은 거리를 구함
def bfs2(z):
    global answer
    dist = [[-1] * n for _ in range(n)] # 거리가 저장될 배열
    q = deque()

    for i in range(n):
        for j in range(n):
            if arr[i][j] == z:
                q.append([i, j])
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 갈 수 없는 곳이면 continue
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 다른 땅을 만나면 기존 답과 비교하여 짧은 거리 선택
            if arr[nx][ny] > 0 and arr[nx][ny] != z:
                answer = min(answer, dist[x][y])
                return
            # 바다를 만나면 dist를 1씩 늘림
            if arr[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx, ny])


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
vis = [[False] * n for _ in range(n)]
count = 1
answer = sys.maxsize

for i in range(n):
    for j in range(n):
        if not vis[i][j] and arr[i][j] == 1:
            bfs1(i, j)
            count += 1

for i in range(1, count):
    bfs2(i)

print(answer)
