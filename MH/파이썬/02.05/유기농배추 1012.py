#문제목록에는 없지만 dfs를 연습하기 위해서 푼 문제
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x,y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if board[x][y] == 1:
        board[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

num = int(input())
for _ in range(num):
    n,m,k = map(int,input().split())
    #가로,세로,배추위치개수
    board = [[0]*n for _ in range(m)]
    for _ in range(k):
        a,b = map(int,input().split())
        board[b][a] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if dfs(i,j) == True:
                cnt+=1

    print(cnt)