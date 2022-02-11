import sys
sys.setrecursionlimit(10000)

def dfs(num):
    visit[num] = 1
    for i in board[num]:
        if visit[i] == 0:
            dfs(i)
    

for _ in range(int(input())):
    num = int(input())
    arr = [0]+ list(map(int,input().split()))
    board = [[] for _ in range(num+1)]
    for i in range(1,num+1):
        board[i].append(arr[i])
        board[arr[i]].append(i)
    visit = [0 for _ in range(num+1)]
    cnt = 0
    for i in range(1,num+1):
        if visit[i] == 0:
            dfs(i)
            cnt+=1
    print(cnt)

