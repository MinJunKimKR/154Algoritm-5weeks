#2251
#실버


#bfs로 접근해보자..
from collections import deque

f,s,t=map(int,input().split())

visited=[[0 for x in range(201)] for y in range(201)]
visited[0][0]=1
answer=[]

def pour(x,y): #방문체크하는 부분을 따로 함수화.
    
    if visited[x][y]==False:
        visited[x][y]=1
        queue.append([x,y])

def bfs():
    
    
    queue.append([0,0])
    while(queue):
        a,b=queue.popleft()
        c=t-a-b
        
        if(a==0): #첫번째 물통이 비어있다면
            answer.append(c) #출력
        #x-->y
        water=min(a,s-b)
        pour(a-water,b+water)
        
        #x-->z
        water=min(a,t-c)
        pour(a-water,b)
        
        #y-->x
        water=min(b,f-a)
        pour(a+water,b-water)
        
        #y-->z
        water=min(b,t-c)
        pour(a,b-water)
        
        #z-->x
        water=min(c,f-a)
        pour(a+water,b)
        
        #z-->y
        water=min(c,s-b)
        pour(a,b+water)
            
queue=deque()                   
bfs()

answer.sort()
print(*answer)
