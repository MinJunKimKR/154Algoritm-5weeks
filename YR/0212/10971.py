#10971
#실버2

#dfs,bfs는 완전탐색 기반.

#dfs이용.
import sys

n=int(input())

arr=[]

for i in range(n):
    arr.append([int(x) for x in sys.stdin.readline().split()])

#인접 행렬 형태


visited=[0 for i in range(n)] #visited는 1차원이여도됨.

def dfs(cost,start,cur):
    global mincost
    if cost>mincost:
        return
    
    if start==cur and visited.count(False)==0: #처음위치와 마지막위치가 같고 모두 방문했을때
        mincost=min(mincost,cost)
        return
        
    for i in range(n):
        if visited[i]==False and arr[cur][i]!=0:
            visited[i]=1
            dfs(cost+arr[cur][i],start,i)
            visited[i]=0



mincost=sys.maxsize

dfs(0,0,0)
print(mincost)
    
    
    
