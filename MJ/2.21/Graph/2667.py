# 6:10 -> 6:40
# 6:23 [success]
import sys
sys_input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(sys_input().strip()))))

houses = []
vector = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dfs(x, y):
    global this_num, graph
    graph[x][y] = 0
    this_num += 1

    for vec in vector:
        nx = x + vec[0]
        ny = y + vec[1]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if graph[nx][ny] == 1:
            dfs(nx, ny)


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            this_num = 0
            dfs(i, j)
            houses.append(this_num)

print(len(houses))
for i in sorted(houses):
    print(i)


# 5
# 10101
# 10001
# 01001
# 00001
# 10011
