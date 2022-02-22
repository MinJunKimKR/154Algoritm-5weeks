# 12:58 -> 1:28
# 1:12[success]
T = int(input())

for _ in range(T):
    N = int(input())
    visited = [False] * (N+1)
    graph = [0] + list(map(int, input().split()))
    cnt_cycle = 0

    for i in range(1, N+1):
        if visited[i]:
            continue
        start = i
        to = graph[i]
        cnt_cycle += 1
        while start != to:
            visited[to] = True
            to = graph[to]
    print(cnt_cycle)
