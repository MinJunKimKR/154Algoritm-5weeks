#11724
#실버2

#단순히 연결요소의 개수를 구하는 것이므로 dfs인지 bfs인지는 상관없을듯.
#둘다 이용해서 풀이! -> 인접 리스트 이용.

from collections import deque
import sys

sys.setrecursionlimit(10000) #최대 재귀횟수인 1000회를 넘으면 오류나기 때문에 제한을 풀어주기.

n,m=map(int,sys.stdin.readline().split()) # 첫줄 입력받기

visit=[0 for i in range(n+1)]
s=[[] for y in range(n+1)] #인접 행렬이 아닌 인접 리스트 생성.

for i in range(m):
    u,v=map(int,sys.stdin.readline().split())
    s[u].append(v)
    s[v].append(u)
    


def bfs(v):
    queue=deque()
    queue.append(v)
    visit[v]=1
    
    while(queue):
        temp=queue.popleft()
        for i in s[temp]: #연결리스트에서..!
            if visit[i]==False:
                queue.append(i)
                visit[i]=1

def dfs(v):
    visit[v]=1
    
    for i in s[v]:
        if visit[i]==False:
            dfs(i)

cnt=0 #연결 요소 개수 셀 변수
'''
for i in range(1,n+1):
    if visit[i]==False:
        bfs(i)
        cnt+=1
'''

for i in range(1,n+1):
    if visit[i]==False:
        dfs(i)
        cnt+=1

print(cnt)
    
