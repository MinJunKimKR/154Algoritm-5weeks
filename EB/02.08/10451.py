# 10451. 순열 사이클

def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)


import sys
input = sys.stdin.readline

     
for _ in range(int(input())):

    n = int(input())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    
    lst = list(map(int, input().split()))

    for i in range(1, n+1):
        graph[i].append(lst[i-1])
        graph[lst[i-1]].append(i)

    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    
    print(cnt)
