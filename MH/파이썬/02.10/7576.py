from collections import deque
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]

# def dfs(i,j):
#     for x,y in (0,-1),(0,1),(1,0),(-1,0):
#         ni = i+x
#         nj = j+y
#         if ni < 0 or ni >= m or nj < 0 or nj >= n:
#             continue
#         if arr[ni][nj] == 0:
#             arr[ni][nj] = arr[i][j]+1
#             dfs(ni,nj)



def bfs():
    while q:
        x,y = q.popleft()
        for a,b in (0,1),(0,-1),(1,0),(-1,0):
            nx = x+a
            ny = y+b
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y]+1
                q.append((nx,ny))


q = deque()
for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            q.append((i, j))
bfs()
check = False
maxnum = 0
for i in arr:
    if 0 in i:
        check = True
    maxnum = max(maxnum,max(i))

if not check:
    print(maxnum-1)
else:
    print(-1)

