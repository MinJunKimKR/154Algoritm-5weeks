# 6:31 -> 7:01
# 6:54 [Success]
import sys
sys.setrecursionlimit(1000001)
sys_input = sys.stdin.readline

vector = [[1, 0], [-1, 0], [1, 1], [1, -1], [0, 1], [0, -1], [-1, -1], [-1, 1]]


def dfs(h, w):
    global cnt_island
    global graph
    graph[h][w] = 0

    for vec in vector:
        nh, nw = h+vec[0], w+vec[1]
        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if graph[nh][nw] == 1:
            dfs(nh, nw)


while True:
    W, H = map(int, sys_input().strip().split())
    if W+H == 0:
        break
    graph = []
    cnt_island = 0
    for _ in range(H):
        graph.append(list(map(int, sys_input().strip().split())))
    for i in range(H):
        for j in range(W):
            if graph[i][j] == 1:
                cnt_island += 1
                dfs(i, j)
    print(cnt_island)
