#11559
#골드4

#구현
from collections import deque

#bfs이용? -> 맞네!

dx=[0,0,-1,1]
dy=[1,-1,0,0]
def bfs(x,y,color):
    cnt=0
    queue=deque()
    visited=[[0 for i in range(6)] for x in range(12)]
    
    pang=deque()
    pang.append([x,y])
    
    queue.append([x,y])
    
    while(queue):
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<12 and 0<=ny<6 and visited[nx][ny]==False and arr[nx][ny]==color:
                queue.append([nx,ny])
                pang.append([nx,ny])
                visited[nx][ny]=True
                cnt+=1
    
    if cnt>=4:
        for x,y in pang:
            arr[x][y]='.'
        return 1
    return 0

def gravity():
    for y in range(6):
        queue=deque()
        for x in range(11,-1,-1):
            if arr[x][y]!='.':
                queue.append(arr[x][y])
        for x in range(11,-1,-1):
            if queue:
                arr[x][y]=queue.popleft()
            else:
                arr[x][y]='.'                


arr=[]
for i in range(12):
    arr.append(list(input()))
    
result=0
while(1):
    flag=0
    for i in range(12):
        for j in range(6):
            if arr[i][j]!='.':
                if bfs(i,j,arr[i][j]):
                    flag=1
                    
    if flag==1:
        result+=1
    else:
        break
    gravity()

print(result)
