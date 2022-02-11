import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
visit = [False]*(n+1)

def dfs(num):
    visit[num] = True
    for i in arr[num]:
        if not visit[i]:
            dfs(i)

cnt=0
for i in range(1,n+1):
    if not visit[i]:
        dfs(i)
        cnt+=1

print(cnt)