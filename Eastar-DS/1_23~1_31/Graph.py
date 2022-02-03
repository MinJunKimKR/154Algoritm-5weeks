#Graph

#1260
import sys
from collections import defaultdict,deque
n,m,start = map(int,input().split())
graph = defaultdict(set)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)
out1, out2 = [], [start]
def dfs(start):
    if(start not in out1):
        out1.append(start)
    else:
        return
    for s in sorted(list(graph[start])):
        dfs(s)
    return
def bfs(start):
    queue = deque([start])
    while(queue):
        num = queue.popleft()
        for s in sorted(list(graph[num])):
            if(s not in out2):
                queue.append(s)
                out2.append(s)
dfs(start)
bfs(start)
print(' '.join([str(num) for num in out1]))
print(' '.join([str(num) for num in out2]))

import sys
from collections import defaultdict,deque
n,m,start = map(int,sys.stdin.readline().split())
graph = defaultdict(set)
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)
out1, out2 = [], [start]
def dfs(start):
    if(start not in out1):
        out1.append(start)
    else:
        return
    for s in sorted(list(graph[start])):
        dfs(s)
    return
def bfs(start):
    queue = deque([start])
    while(queue):
        num = queue.popleft()
        for s in sorted(list(graph[num])):
            if(s not in out2):
                queue.append(s)
                out2.append(s)
dfs(start)
bfs(start)
print(' '.join([str(num) for num in out1]))
print(' '.join([str(num) for num in out2]))



#11724
import sys,collections
n,m = map(int,sys.stdin.readline().split())
graph,visited,output = collections.defaultdict(list),[0]*n,0
for _ in range(m):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
def bfs(x):
    queue = collections.deque([x])
    while(queue):
        num = queue.popleft()
        for node in graph[num]:
            if(visited[node-1] == 0):
                queue.append(node)
                visited[node-1] = 1    
for i in range(n):
    if(visited[i] == 0):
        output += 1
        bfs(i+1)
print(output)

#dfs
sys.setrecursionlimit(10000)
def dfs(x):
    visited[x-1] = 1
    for node in graph[x]:
        if(visited[node-1] == 0):
            dfs(node)
for i in range(n):
    if(visited[i] == 0):
        output += 1
        dfs(i+1)
print(output)


#1707 삼각형이 있나로 판단하면될듯. sys.stdin.readline
#2그룹으로 나누기
import sys, collections
K = int(input())
for _ in range(K):
    V,E = map(int,input().split())
    graph= collections.defaultdict(list)
    group = [0] * (V+1)
    def existTri():
        queue = collections.deque([list(graph)[0]])
        for key in sorted(list(graph)):
            nodes = graph[key]
            #첫그룹 1
            if(group[key] == 0):
                group[key] = 1
            if(group[key] == 1):
                for node in nodes:
                    if(group[node] == 1):
                        return print('NO')
                    group[node] = -1
            else:
                for node in nodes:
                    if(group[node] == -1):
                        return print('NO')
                    group[node] = 1             
        return print('YES')
    for _ in range(E):
        u,v = map(int,input().split())
        if(u < v):
            graph[u].append(v)
        else:
            graph[v].append(u)
    existTri()



#시간초과
import sys, collections
K = int(input())
for _ in range(K):
    V,E = map(int,input().split())
    graph= collections.defaultdict(list)
    def existTri():
        for key in sorted(list(graph)):
            nodes = sorted(graph[key])
            length = len(graph[key])
            for i in range(length-1):
                for j in range(i+1,length):
                    if(nodes[j] in graph[nodes[i]]):
                        return print('NO')                        
        return print('YES')
    for _ in range(E):
        u,v = map(int,input().split())
        if(u < v):
            graph[u].append(v)
        else:
            graph[v].append(u)
    existTri()


#메모리초과
import sys
K = int(input())
for _ in range(K):
    V,E = map(int,input().split())
    graph= [[0]*(V-i) for i in range(V)]
    def existTri():
        if(V in [1,2]):
            return print('YES')
        for key in range(V):
            for i in range(key+1, V - 1):
                if(graph[key][i-key] == 1):
                    for j in range(i+1,V):
                        if(graph[key][j-key] ==1 and graph[i][j-i] == 1):
                            return print('NO')                        
        return print('YES')
    for _ in range(E):
        u,v = map(int,input().split())
        if(u<v):
            graph[u-1][v-u] = 1
        else:
            graph[v-1][u-v] = 1
    existTri()




































