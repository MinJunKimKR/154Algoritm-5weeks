#2178
#실버1

#최단 거리므로 bfs!
#어려운 문제는 아닌듯..그래도 입력부분 조심하쟈 ㅜㅡㅜ
from collections import deque

m,n=map(int,input().split())
arr=[]
queue=deque([])

dx=[0,0,-1,1]
dy=[1,-1,0,0]
for i in range(m):
    arr.append(list(map(int,input())))

def bfs(a,b):
    queue.append([a,b])
    while(queue):
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if arr[nx][ny]==1:
                    queue.append([nx,ny])
                    arr[nx][ny]=arr[x][y]+1



bfs(0,0)

print(arr[m-1][n-1])
