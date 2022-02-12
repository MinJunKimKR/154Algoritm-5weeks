from collections import deque
import sys
sys.setrecursionlimit(10**9)

num = int(input())
arr = [[] for i in range(num+1)]
check = [False] * (num+1)
parents = [0 for _ in range(num+1)]

# def bfs():
#     q = deque()
#     q.append(1)
#     while q:
#         x = q.popleft()
#         for i in arr[x]:
#             if parents[i] == 0:
#                 parents[i] = x
#                 q.append(i)

def dfs(i):
    check[i] = True
    for a in arr[i]:
        if parents[a] == 0 and not check[a]:
            parents[a] = i
            dfs(a)



for _ in range(num-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

#bfs()
dfs(1)


for i in parents[2:num+1]:
    print(i)