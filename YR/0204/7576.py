#7576
#골드5

#보관후 하루가 지나면 익은토마토의 상하좌우에 있는 익지않은 토마토는 익음.
#몇일이 지나면 다 익는지 ! -> 토마토가 모두 익지 못하는 상황이면 -1출력
#visited 배열은 따로 필요없을듯!
#dfs가 아니라 bfs로 가야할듯.

from sys import modules
from collections import deque

m,n=map(int,input().split())

arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))
    
dx=[0,0,-1,1]
dy=[1,-1,0,0] 

queue=deque([])

def bfs():
    while(queue):
        tx,ty=queue.popleft()
        for i in range(4):
            nx=tx+dx[i]
            ny=ty+dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny]==0:
                    queue.append([nx,ny])
                    arr[nx][ny]=arr[tx][ty]+1
                
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            queue.append([i,j]) #익은 토마토 넣어주기
bfs()           
cnt=-1
for i in arr:
    for j in i: #안익은 토마토가 있는지 check.
        if j==0:
            print(-1)
            quit()
        cnt=max(cnt,j)

print(cnt-1)
    
