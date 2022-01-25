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


#1707 삼각형이 있나로 판단하면될듯.
import sys, collections
K = int(input())
for _ in range(K):
    V,E = map(int,input().split())
    graph,visited = collections.defaultdict(list),[]
    def existTri():
        for key in list(graph):
            nodes = graph[key]
            for node in nodes:
                if(node in visited):
                    continue
                second_nodes = graph[node]
                for second_node in second_nodes:
                    if(second_node in visited):
                        continue
                    if(key in graph[second_node]):
                        print('NO')
                        return
            visited.append(key)
        return print('YES')
    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    existTri()
    # for key in list(graph):
    #     nodes = graph[key]
    #     for node in nodes:
    #         if(node in visited):
    #             continue
    #         second_nodes = graph[node]
    #         for second_node in second_nodes:
    #             if(second_node in visited):
    #                 continue
    #             if(key in graph[second_node]):
    #                 print('NO')
    #                 break
    #     visited.append(key)
    # print('YES')

import sys, collections
K = int(sys.stdin.readline())
for _ in range(K):
    V,E = map(int,sys.stdin.readline().split())
    graph,visited = collections.defaultdict(list),[]
    def existTri():
        for key in list(graph):
            nodes = graph[key]
            for node in nodes:
                if(node in visited):
                    continue
                second_nodes = graph[node]
                for second_node in second_nodes:
                    if(second_node in visited):
                        continue
                    if(key in graph[second_node]):
                        print('NO')
                        return
            visited.append(key)
        return print('YES')
    for _ in range(E):
        u,v = map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    existTri()








































