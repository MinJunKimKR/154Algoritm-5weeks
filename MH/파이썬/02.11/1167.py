from sys import stdin
from collections import deque

read = stdin.readline
V = int(read())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    c = list(map(int, read().split()))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))


def bfs(start):
    visit = [-1] * (V + 1)
    que = deque()
    que.append(start)
    visit[start] = 0
    _max = [0, 0]

    while que:
        t = que.popleft()
        for e, w in graph[t]:
            if visit[e] == -1:
                visit[e] = visit[t] + w
                que.append(e)
                if _max[0] < visit[e]:
                    _max = visit[e], e

    return _max


dis, node = bfs(1)
dis, node = bfs(node)
print(dis)

