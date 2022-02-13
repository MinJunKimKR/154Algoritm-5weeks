import sys
sys.setrecursionlimit(10**6)

def dfs(i,j):
    global cnt
    if 0 > i or i >= num or 0 > j or j >= num:
        return False
    if arr[i][j] == 1:
        cnt+=1
        arr[i][j] = 0
        for x,y in (0,-1),(0,1),(1,0),(-1,0):
            ni = x+i
            nj = y+j
            dfs(ni,nj)
        return True


num = int(input())
arr = [list(map(int,input())) for _ in range(num)]
ans = []
cnt = 0

for i in range(num):
    for j in range(num):
        if dfs(i,j) == True:
            ans.append(cnt)
            cnt = 0

print(len(ans))
ans.sort()
for i in ans:
    print(i)