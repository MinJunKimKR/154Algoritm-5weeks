#9019
#골드4
#딱봐도 bfs쓰는 문제

from collections import deque
import sys


def bfs(inp,target):
    queue=deque()
    
    queue.append([inp,'']) #명령어도 같이 넘겨줌.
    
    while queue:
        temp,currentst=queue.popleft()
        dic={0:'D',1:'S',2:'L',3:'R'}
        
        if temp==target:
            print(currentst)
            return

        st=str(temp)
        if temp==0:
            value=9999
        else:
            value=temp-1
        j=0
        for i in [(temp*2)%10000,value,int(temp % 1000 * 10 + temp / 1000), int(temp % 10 * 1000 + temp // 10)]:
            if visited[i]==False and i<10000:
                visited[i]=1
                queue.append([i,currentst+dic[j]])
            j+=1

n=int(input())         

#int(st[1:]+st[0])
#int(st[-1]+st[0:len(st)-1])

for i in range(n):
    visited=[0 for i in range(10000)]
    inp,target=map(int,sys.stdin.readline().split())
    bfs(inp,target)
