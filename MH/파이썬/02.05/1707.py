#이분 그래프
#인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두 가지 색으로만 칠할 수 있는 그래프
# from collections import deque
#
# def bfs(num):
#     q = deque()
#     q.append(num)
#     visit[num] = 1
#     while q:
#         x = q.popleft()
#         for i in board[x]:
#             if visit[i] == 0:
#                 visit[i] = -visit[x]
#                 q.append(i)
#             else:
#                 if visit[i] == visit[x]:
#                     return False
#     return True
#
#
# num1 = int(input())
# for i in range(num1):
#     n,m = map(int, input().split())
#     board = [[] for _ in range(n+1)]
#     visit = [0] * (n + 1)
#     flag = 1
#     for _ in range(m):
#         a,b = map(int,input().split())
#         board[a].append(b)
#         board[b].append(a)
#
#     for i in range(1,n+1):
#         if visit[i] == 0:
#             if not bfs(i):
#                 flag = -1
#                 break
#     print('YES' if flag == 1 else 'NO')

import sys
sys.setrecursionlimit(10000)

def dfs(now,group):
    visit[now] = group
    for i in arr[now]:
        #안 가본 곳
        if visit[i] == 0:
            if not dfs(i,-group):
                return False
        #가봤는데 색깔이 같으면
        elif visit[i] == visit[now]:
            return False
    return True

num = int(input())
for _ in range(num):
    n,m = map(int,input().split())
    arr = [[] for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)
    ans = True
    for i in range(1,n+1):
        if visit[i] == 0:
            ans = dfs(i,1)
            if not ans:
                break
    print("YES" if ans else "NO")






