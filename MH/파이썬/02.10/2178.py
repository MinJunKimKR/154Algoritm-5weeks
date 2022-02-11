from collections import deque

n,m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]
check = [[False]*m for _ in range(n)]


def bfs(i,j):
    q = deque()
    q.append((i,j))
    check[i][j] = True
    while q:
        x,y = q.popleft()
        for a,b in (0,1),(0,-1),(1,0),(-1,0):
            ni = x+a
            nj = y+b
            if 0 > ni or ni >= n or 0 > nj or nj >= m:
                continue
            if arr[ni][nj] == 1 and not check[ni][nj]:
                arr[ni][nj] = arr[x][y]+1
                q.append((ni,nj))

# def dfs(i,j):
#     check[i][j] = True
#     for a,b in (0,1),(0,-1),(1,0),(-1,0):
#         ni = i+a
#         nj = j+b
#         if 0 > ni or ni >= n or 0 > nj or nj >= m:
#             continue
#         if arr[ni][nj] == 1 and not check[ni][nj]:
#             arr[ni][nj] = arr[i][j]+1
#             dfs(ni,nj)

bfs(0,0)

print(arr[n-1][m-1])

