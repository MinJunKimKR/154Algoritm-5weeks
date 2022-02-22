# 2:10 -> 2:40
# 2:29[Success]
import sys
sys.setrecursionlimit(100000)
sys_input = sys.stdin.readline
T = int(input())
vector = [[1, 0], [-1, 0], [0, 1], [0, -1]]


for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    cnt_worm = 0

    def bfs(x, y):
        global graph
        graph[x][y] = 0
        for vec in vector:
            nx = x+vec[0]
            ny = y+vec[1]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if graph[nx][ny] == 1:
                bfs(nx, ny)
    for _ in range(K):
        x, y = map(int, sys_input().strip().split())
        graph[y][x] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                cnt_worm += 1
                bfs(i, j)
    print(cnt_worm)
