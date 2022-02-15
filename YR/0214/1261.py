#1261
#골드 4
from collections import deque
import sys

m,n=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list((map(int,input()))))

visited=[[-1 for i in range(m)]for x in range(n)]
dx=[0,0,-1,1]
dy=[1,1,0,0]
visited[0][0]=0
def bfs():
    global ans
    queue=deque()
    queue.append([0,0]) #0,0에서 시작
    
    while queue:
        x,y=queue.popleft()
        
        if (x,y)==(n-1,m-1):
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1:
                
                if arr[nx][ny]==0:
                   
                    visited[nx][ny]=visited[x][y]
                    queue.appendleft([nx,ny]) #왜 appendleft..? 우선적으로 가야해서 그런가봄
                else:
                    visited[nx][ny]=visited[x][y]+1
                    queue.append([nx,ny])

bfs()
print(visited[n-1][m-1])
