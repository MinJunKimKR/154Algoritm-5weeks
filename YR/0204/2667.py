#2667
#실버1

#dx,dy테크닉 사용해야하나? ->일단 사용해봄.
#상하좌우로 맞닿아있으면 연결된것.

#dfs인지 bfs인지 먼저 판단. ->dfs든 bfs든 상관없을듯.(거리계산 등이 아닌 연결여부를 확인하는 것이므로)

#인접리스트가 아닌 인접행렬.

n=int(input())
arr=[]

visited=[[0 for i in range(n+1)] for x in range(n+1)]


for i in range(n):
    arr.append(list(map(int,input())))
        

#visited배열이 필요가 없는게, 방문한다음 0을 넣어주면됨.

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y):
    global cnt
    visited[x][y]=1 #방문 처리.  
    cnt+=1
    
    for i in range(4):

        nx=x+dx[i]
        ny=y+dy[i] #dx,dy 테크닉 사용하기 위해서
       
        if 0<=nx<n and 0<=ny<n: #범위 체크.
            if arr[nx][ny]==1 and visited[nx][ny]==False:
                dfs(nx,ny)
    
graph=[] #결과를 저장할 배열.  
cnt=0

for i in range(n):
    for j in range(n):
        if arr[i][j]==1 and visited[i][j]==False:
            cnt=0
            dfs(i,j)
            graph.append(cnt)
            
            
            
print(len(graph))
graph.sort()
for g in graph:
    print(g)
            
