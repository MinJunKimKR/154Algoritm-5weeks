#5014
#골드5
from collections import deque
import sys

input=sys.stdin.readline
total,start,target,up,down=map(int,input().split())

#dfs가 아니라 bfs.ㅜㅜ
#이게 왜 골드..?


def bfs(v,cnt):
    visited=[0 for i in range(total+1)]
    queue=deque()
    queue.append(v)
    
    while(queue):
        temp=queue.popleft()
        
        if temp==target:
            print(visited[temp])
            return
        
        if 0<temp+up<=total and visited[temp+up]==False and temp+up!=v:
            visited[temp+up]=visited[temp]+1
            queue.append(temp+up)
        if 0<temp-down<=total and visited[temp-down]==False and temp-down!=v:
            visited[temp-down]=visited[temp]+1
            queue.append(temp-down)
    
    print("use the stairs")  
        

bfs(start,0)
       
