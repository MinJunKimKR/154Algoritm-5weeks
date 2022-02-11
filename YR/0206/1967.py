#1967
#골드4

#앞문제와 거의 비슷해보임.이 아니라 똑같아보임
import sys
sys.setrecursionlimit(10**9)

n=int(input())
graph=[[] for _ in range(n+1)] #인접리스트 형식

for _ in range(n-1):
    w = list(map(int,input().split()))
    graph[w[0]].append([w[1], w[2]]) #[연결노드, 가중치] 형식으로 저장.
    graph[w[1]].append([w[0], w[2]])
visited=[-1 for i in range(n+1)]
visited[1]=0

def dfs(v,d):
    for i,j in graph[v]:
        if visited[i]==-1:
            visited[i]=d+j #visited배열의 값을 탐색하기까지 걸린 간선의 거리로 초기화
            dfs(i,d+j)
            
dfs(1,0)

mxidx=visited.index(max(visited))
visited=[-1 for i in range(n+1)]

visited[mxidx]=0#(거리가 0이므로)
dfs(mxidx,0)

#트리의 지름을 구하는 방법 : 노드 x에서 가장 먼 노드 y를 찾고 그 y에서 가장 먼 노드까지의 거리가 트리의 지름.
print(max(visited))

    
    
