#11725
#실버2
#dfs로 접근해야 하는지는 진짜 몰랐음 ㅜㅜ
import sys
sys.setrecursionlimit(1000000)

n=int(input())

#인접리스트로 진행하면 될듯.

tree=[[]for _ in range(n+1)]
parent=[0 for i in range(n+1)]

for i in range(n-1):
    m,n=map(int,input().split())
    tree[m].append(n)
    tree[n].append(m)
    
def dfs(v):
    
    for i in tree[v]:
        if parent[i]==0:
            parent[i]=v
            dfs(i)
    
dfs(1)
 
for i in range(2,n+1):
    print(parent[i])


    
