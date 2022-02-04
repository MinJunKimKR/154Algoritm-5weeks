#1707
#골드4

import sys

sys.setrecursionlimit(10000000) #최대 재귀횟수인 1000회를 넘으면 오류나기 때문에 제한을 풀어주기.

num=int(input())

for i in range(num):
    n,m=map(int,sys.stdin.readline().split()) 
    
    s=[[] for i in range(n+1)] #인접 리스트
    visit=[0 for i in range(n+1)]

    for i in range(m):
        u,v=map(int,sys.stdin.readline().split())
        s[u].append(v)
        s[v].append(u)
    
    def dfs(v,group):
        visit[v]=group
        
        for i in s[v]:
            if visit[i]==0:
                a=dfs(i,-group)
                if a==False:
                    return False
            elif visit[i]==visit[v]: #방문을 했다해도 색깔이 같으면 취소.
                return False
            
        return True
                
    ans=True
    for i in range(1,n+1):
        if visit[i]==0:
            if dfs(i,1)==False:
                ans=False
                break
            
    print('YES' if ans else 'NO')
            
    

