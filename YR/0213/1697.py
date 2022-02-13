#1697
#실버1

#완전탐색

#점의 범위가 매우 작음.(0과 10만사이.)
# DFS 방식은 최소 길이, 최소 거리와 같은 최소 경로를 구하는 데 있어서는 비효율적이다. 오히려 BFS는 이러한 최소 길이를 구하는 데 있어서 더 효율적이라고 볼 수 있다

#따라서 bfs이용.


import sys
from collections import deque

n,k=map(int,input().split())

visited=[0 for i in range(100001)]


def bfs():
    queue=deque()
    queue.append(n)
    
    while queue:
        x=queue.popleft()
        if x==k:
            print(visited[x])
            break
        for i in [x+1,x-1,x*2]:
            if 0<=i<10**5+1:
                if visited[i]==False:
                    visited[i]=visited[x]+1
                    queue.append(i)
        

bfs()
    
        
    
    
