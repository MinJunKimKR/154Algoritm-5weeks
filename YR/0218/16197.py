#16197
#골드4

#최소 거리를 구해야하기 때문에 bfs나 dfs를 쓰는게 맞을듯..
#bfs사용

from collections import deque

n,m=map(int,input().split())

board=[]

board.append([0]*(m+2))
for i in range(n):
    board.append([0]+list(input())+[0])
board.append([0]*(m+2)) #상하좌우에 0을 추가해서 값이 0이면 범위를 벗어난것으로 판단.

cur=[]
for i in range (n+2):
    for j in range (m+2):
        if board[i][j]=='o':
            cur.append(i)
            cur.append(j)
            board[i][j]='.'
     
#만약 두 동전의 y좌표가 같다면 -> x좌표로 이동하여 떨어뜨리기 가능
#x좌표가 같다면: y좌표로 이동하여 떨어뜨리기 가능.
#둘다 다르다면: 자유롭게 이동.

dx=[0,0,-1,1]
dy=[1,-1,0,0]

visited=[[[[0 for i in range(m+2)] for j in range(n+2)] for x in range(m+2)] for y in range(n+2)]
visited[cur[0]][cur[1]][cur[2]][cur[3]]=1

def bfs(x1,y1,x2,y2):
    queue=deque()
    queue.append([x1,y1,x2,y2])
    
    while(queue):
        x1,y1,x2,y2=queue.popleft()
        
        if visited[x1][y1][x2][y2]>10:
            break
        
        for i in range(4):
            nx1=x1+dx[i]
            ny1=y1+dy[i]
            
            nx2=x2+dx[i]
            ny2=y2+dy[i]
            
            if board[nx1][ny1]==0 and board[nx2][ny2]==0: #두개의 동전 모두 범위를 벗어났을 때
                continue
            
            if board[nx1][ny1]==0: 
                return visited[x1][y1][x2][y2]
            if board[nx2][ny2]==0: 
                return visited[x1][y1][x2][y2] #누적된 count return (조건만족)
            
            if board[nx1][ny1]=='#': nx1,ny1=x1,y1
            if board[nx2][ny2]=='#': nx2,ny2=x2,y2
            
            if visited[nx1][ny1][nx2][ny2]==False:
                queue.append([nx1,ny1,nx2,ny2])
                visited[nx1][ny1][nx2][ny2]=visited[x1][y1][x2][y2]+1 #count 세주기 위함.
    
    return -1

print(bfs(cur[0],cur[1],cur[2],cur[3]))
   
