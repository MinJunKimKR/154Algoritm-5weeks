from collections import deque
n,m,k = map(int,input().split())
#정점,간선,시작하는 점
board=[[0]*n for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    board[a-1][b-1] = 1
    board[b-1][a-1] = 1
visit2 = [False]*n

def dfs(num):
    visit2[num]=True
    print(num+1,end=" ")
    for i in range(n):
        if board[num][i] == 1 and visit2[i] == False:
            dfs(i)

def bfs(num):
    visit = [False]*n
    q = deque()
    q.append(num)
    visit[num] = True
    while q:
        x = q.popleft()
        print(x+1,end=" ")
        for i in range(n):
            if board[x][i] == 1 and visit[i] == False:
                q.append(i)
                visit[i] = True

dfs(k-1)
print()
bfs(k-1)