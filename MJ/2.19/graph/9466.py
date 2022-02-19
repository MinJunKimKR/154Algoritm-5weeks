# 1:40 -> 2:20
# 1:57[GG]
T = int(input())


def dfs(start, from_num, to, team):
    global cnt, visited
    if visited[to]:
        cnt += len(team)
        return
    visited[to] = True
    if graph[to] == start:
        return
    dfs(start, to, graph[to], team+[from_num])


for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)
    cnt = 0
    for i in range(1, n):
        if visited[i]:
            cnt += 1
            continue
        visited[i] = True
        dfs(i, i, graph[i], [])
    print(cnt)
