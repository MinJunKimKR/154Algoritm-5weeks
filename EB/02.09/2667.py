# 2667. 단지번호 붙이기 - 풀이 보충

import sys

def dfs(x, y):
    global cnt

    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0 # visited로 구분하지 않고, 0으로 변경

        for i in range(4):
            dfs(x+dx[i], y+dy[i])

        return True

n = int(sys.stdin.readline())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

grp = []
cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            grp.append(cnt)
            cnt = 0

print(len(grp))
grp.sort()
for i in grp:
    print(i)
