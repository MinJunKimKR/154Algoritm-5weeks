# 2:24-> 3:04
# 2:35 [no idea]
# 2:44 [restart] -> 3:24
# 3:21[Success]
# refer : https://sdesigner.tistory.com/52
import sys
sys_input = sys.stdin.readline

N, M = map(int, input().split())
graph = []

max_total = 0
for _ in range(N):
    graph.append(list(map(int, list(sys_input().strip()))))


def cal_arr(sx, ex, sy, ey):
    total = 0
    for i in range(sx, ex):
        for j in range(sy, ey):
            total += graph[i][j]
    return total


# # 가로로 3줄 쪼개기
for i in range(1, N-1):
    for j in range(i+1, N):
        first = cal_arr(0, i, 0, M)
        second = cal_arr(i, j, 0, M)
        third = cal_arr(j, N, 0, M)
        max_total = max(max_total, first*second*third)

# # 세로로 3줄 쪼개기
for i in range(1, M-1):
    for j in range(i+1, M):
        first = cal_arr(0, N, 0, i)
        second = cal_arr(0, N, i, j)
        third = cal_arr(0, N, j, M)
        max_total = max(max_total, first*second*third)

# 가로 2개 세로 1
for i in range(1, N):
    for j in range(1, M):
        first = cal_arr(0, i, 0, j)
        second = cal_arr(i, N, 0, j)
        third = cal_arr(0, N, j, M)
        max_total = max(max_total, first*second*third)

# 세로 1 가로 2
for i in range(1, M):
    for j in range(1, N):
        first = cal_arr(0, N, 0, i)
        second = cal_arr(0, j, i, M)
        third = cal_arr(j, N, i, M)
        max_total = max(max_total, first*second*third)


# 가로 2 가로 1
for i in range(1, N):
    for j in range(1, M):
        first = cal_arr(0, i, 0, j)
        second = cal_arr(0, i, j, M)
        third = cal_arr(i, N, 0, M)
        max_total = max(max_total, first*second*third)

# 가로 1 가로 2
for i in range(1, N):
    for j in range(1, M):
        first = cal_arr(0, i, 0, M)
        second = cal_arr(i, N, 0, j)
        third = cal_arr(i, N, j, M)
        max_total = max(max_total, first*second*third)
print(max_total)
