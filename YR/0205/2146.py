#2146
#골드3 
#bfs선택.
# 각섬에 번호를 붙혀서 그룹핑먼저 한후에 진행.(dfs이용)
from collections import deque

import sys
sys.setrecursionlimit(1000000)

n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

visited=[[0 for i in range(n)]for x in range(n)]



dx=[0,0,-1,1]
dy=[1,-1,0,0]

def dfs(x,y): # 각섬에 번호를 붙이기.
    global cnt
    visited[x][y]=1
    arr[x][y]=cnt

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if visited[nx][ny]==False and arr[nx][ny]==1:
                dfs(nx,ny)

def bfs(num):
    global ans
    queue=deque([])
    dist=[[-1 for i in range(n)]for x in range(n)] #거리 계산 용도 배열
    
    for i in range(n):
        for j in range(n):
            if arr[i][j]==num:
                queue.append([i,j])
                dist[i][j]=0 #바다는 dist값이 -1, 땅은 0
    while(queue):
        x,y=queue.popleft() 
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                #바다 일때
                if arr[nx][ny]==0 and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[x][y]+1 #거리를 더해줌
                    queue.append([nx,ny])
                #다른 섬에 도착했을때
                if arr[nx][ny]>0 and arr[nx][ny]!=num:
                    ans=min(ans,dist[x][y])
                    return

#각 섬에 번호 붙여주기
cnt=1
for i in range(n):
    for j in range(n):
        if visited[i][j]==False and arr[i][j]==1:
            dfs(i,j)
            cnt+=1

ans=sys.maxsize
for i in range(1,cnt):
    bfs(i)

print(ans)



    
