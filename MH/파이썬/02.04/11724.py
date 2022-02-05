import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int,input().split())
visit = [False]*(n+1)

board = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    # board[a-1][b-1] = 1
    # board[b-1][a-1] = 1
    board[a].append(b)
    board[b].append(a)


def dfs(num):
    visit[num] = True
    for i in board[num]:
        # if board[num][i]==1 and visit[i] == False:
        #     dfs(i)
        if not visit[i]:
            dfs(i)

cnt = 0
for i in range(1,n+1):
    if not visit[i]:
        dfs(i)
        cnt+=1
print(cnt)