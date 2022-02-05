#4963
#실버2
#dfs로 풀이.
import sys
sys.setrecursionlimit(100000)

while(1):
    m,n=map(int,input().split())
    if m==0 and n==0:
        quit()
        
    arr=[]

    for i in range(n):
        arr.append(list(map(int,input().split())))

    visited=[[0 for i in range(m)] for x in range(n)] #방문 check
    #지나온곳을 0으로 바꿔주는 방법을 사용해도 좋음!

    #상하좌우, 대각선까지 check.

    dx=[1,-1,0,0,-1,1,1,-1]
    dy=[0,0,-1,1,1,1,-1,-1]
    #인접행렬.

    def dfs(x,y):
        visited[x][y]=1
        
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if(0<=nx<n and 0<=ny<m): #범위체크
                if visited[nx][ny]==False and arr[x][y]==1:
                    dfs(nx,ny)
                    
                    
    cnt=0 #섬의 개수 카운팅.          
    for i in range(n):
        for j in range(m):
            if visited[i][j]==False and arr[i][j]==1:
                dfs(i,j)
                cnt+=1
                
    print(cnt)
    

