import sys
sys.setrecursionlimit(10**6)

def dfs(i,j):
    if i < 0 or i >= b or j < 0 or j >= a:
        return False
    if arr[i][j] == 1:
        arr[i][j] = 0
        for x,y in (-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1):
            ni = x+i
            nj = y+j
            dfs(ni,nj)
        return True


while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    arr = [list(map(int,input().split())) for _ in range(b)]
    cnt = 0
    for i in range(b):
        for j in range(a):
            if dfs(i,j) == True:
                cnt+=1
    print(cnt)