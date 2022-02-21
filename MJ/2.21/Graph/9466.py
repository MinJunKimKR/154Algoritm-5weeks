# 1:40 -> 2:20
# 1:57[GG]
# 5:05 -> 5:45
# 5:45[memory overflow]
# 6:11 [Success]
import sys
sys.setrecursionlimit(1000001)
T = int(input())


def dfs(from_idx, to):
    global visited, team
    visited[from_idx] = True
    if visited[to]:
        if to in team:
            idx = team.index(to)
            if idx != 0:
                return len(team[:idx])
            else:
                return 0
        return len(team)
    team.append(to)
    return dfs(to, graph[to])


for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            team = [i]
            cnt += dfs(i, graph[i])
    print(cnt)

# arr = [1, 23, 4]
# print(arr.index(1))

# 3
# 10
# 1 3 2 5 6 4 6 9 10 9
# 3
# 1 2 3
# 1
# 5
# 3 3 1 2 1
