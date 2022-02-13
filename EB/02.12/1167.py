# 1167. 트리의 지름

import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
dist = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

print(visited)
for i in range(1, n+1):
    line = list(map(int, input().split()))
    line = line[:-1]
    v = line[0]
    
    for i in range(1, len(line), 2):
        if graph[v].count(line[i]) == 0:
            graph[v].append(line[i])
            graph[line[i]].append(v)
        dist[v].append(line[i+1])

def dfs(n):
    global length
    
    visited[n] = True
    next = graph[n]
    print(dist[n])
    length += dist[n]
    
    if not vistied[next]:
        dfs(next)

length = 0

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
            
    

        
print(graph)
print(dist)
print(length)

'''
    for i in range(1, len(line), 2):
        v = line[0]
        tree[v] = [line[i], line[i+1]]
    '''
    #print(tree)
    #tree[line[0]].append([tree[1], tree[2]])
    


