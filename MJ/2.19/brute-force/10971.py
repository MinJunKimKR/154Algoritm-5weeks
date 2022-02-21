# 6:03 -> 6:33
# 6:30 [FAIL]
# 8:37 [생각을 아예 잘못하고 있었음]
# 9:03 [pass]
import sys
sys_input = sys.stdin.readline
N = int(input())
graph = []
city = [x for x in range(N)]
for _ in range(N):
    graph.append(list(map(int, sys_input().strip().split())))

INF = 100000001*N
min_cost = INF


def dfs(start, next, cost, visited):
    global min_cost
    if len(visited) == N and graph[next][start] != 0:
        min_cost = min(min_cost, cost+graph[next][start])
        return

    for i in range(N):
        this_cost = cost+graph[next][i]
        if i not in visited and this_cost < min_cost and graph[next][i] != 0:
            visited.append(i)
            dfs(start, i, this_cost, visited)
            visited.pop()


for i in range(N):
    dfs(i, i, 0, [i])

print(min_cost)

# def dfs(from_city, to, cost, visited):
#     global min_cost
#     if len(visited) == N and graph[visited[-1]][visited[0]] != 0:
#         min_cost = min(min_cost, cost+graph[visited[-1]][visited[0]])
#         return
#     if graph[from_city][to] == 0:
#         return
#     cost += graph[from_city][to]
#     visited.append(to)
#     for i in range(N):
#         if i not in visited:
#             dfs(to, i, cost, visited)


# for i in range(N):
#     for j in range(N):
#         if i != j and graph[i][j] != 0:
#             dfs(i, j, 0, [i])


# route_arr = list(permutations(city))

# for route in route_arr:
#     if graph[route[-1]][route[0]] == 0:
#         continue
#     total = 0
#     is_not_finish = False
#     for i in range(N-1):
#         if graph[route[i]][route[i+1]] == 0:
#             is_not_finish = True
#             break
#         total += graph[route[i]][route[i+1]]
#         if total >= min_cost:
#             is_not_finish = True
#             break
#     if is_not_finish:
#         continue
#     total += graph[route[-1]][route[0]]
#     min_cost = min(min_cost, total)

# print(min_cost)
