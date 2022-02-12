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


#10451
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(int(n) - 1 for n in input().split())
    visited,output = [0]*N, 0
    for i,num in enumerate(nums):
        if(visited[i] == 0):
            output += 1
            while(visited[i] == 0):
                visited[i] = 1
                i = nums[i]
    print(output)

#최고로 줄인거
import sys
for _ in range(int(sys.stdin.readline())):
    visited,output = [0]*int(sys.stdin.readline()), 0
    nums = list(int(n) - 1 for n in sys.stdin.readline().split())    
    for i,num in enumerate(nums):
        if(visited[i] == 0):
            output += 1
            while(visited[i] == 0):
                visited[i] = 1
                i = nums[i]
    print(output)


#2331
A,P = map(int,input().split())
D = []
while(A not in D):
    D.append(A)
    A = sum([int(a)**P for a in str(A)])
print(D.index(A))


#9466 개어렵네 진짜ㅏㅏㅏ global이라는 좋은기능을 알았따!!!
import sys
sys.setrecursionlimit(200000)
def dfs(i):
    visited[i] = 1
    cycle.append(i)
    if(visited[nums[i]] == 1):
        if(nums[i] in cycle):
            # output += len(cycle[cycle.index(nums[i]):])
            output.append(len(cycle[cycle.index(nums[i]):]))
        return
    else:
        dfs(nums[i])
# input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    nums = [0] + list(map(int,input().split()))
    visited = [1]+[0]*n
    output = []
    for i in range(1,n+1):
        if(visited[i] ==0):
            cycle = []
            dfs(i)
    print(n-sum(output))


#2667
def isConnected(i,j,o):
    #연결된거 0으로 바꿔주면서 넓이체크
    if(i<0 or i>N-1 or j<0 or j>N-1 or nums[i][j] == 0):
        return o
    o += 1
    nums[i][j] = 0
    o = isConnected(i-1,j,o)
    o = isConnected(i+1,j,o)
    o = isConnected(i,j-1,o)
    o = isConnected(i,j+1,o)
    return o
N = int(input())
nums,output = [],[]
for _ in range(N):
    nums.append([int(s) for s in list(input())])
for i in range(N):
    for j in range(N):
        if(nums[i][j] == 1):
            output.append(isConnected(i,j,0))
output.sort()
print(len(output))
for num in output:
    print(num)


# [[0, 1, 1, 0, 1, 0, 0],
#  [0, 1, 1, 0, 1, 0, 1],
#  [1, 1, 1, 0, 1, 0, 1],
#  [0, 0, 0, 0, 1, 1, 1],
#  [0, 1, 0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 1, 1, 0],
#  [0, 1, 1, 1, 0, 0, 0]]


#4963
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
def isLand(i,j):
    if(i<0 or i>h-1 or j<0 or j>w-1 or nums[i][j] == 0):
        return
    nums[i][j] = 0
    isLand(i+1,j)
    isLand(i,j+1)    
    isLand(i+1,j+1)
    isLand(i-1,j+1)   
    isLand(i+1,j-1)
    isLand(i,j-1)
    isLand(i-1,j)
    isLand(i-1,j-1)
    return
    
while(1):
    w,h = map(int,input().split())
    if(w==0 and h==0):
        break
    nums = []
    for _ in range(h):
        nums.append(list(map(int,input().split())))
    #
    output = 0
    for i in range(h):
        for j in range(w):
            if(nums[i][j] == 1):
                isLand(i,j)
                output += 1
    print(output)


#7576
import sys, collections
input = sys.stdin.readline
M,N = map(int,input().split())
nums,queue,day = [], collections.deque([]),0
for i in range(N):
    line = list(map(int,input().split()))
    nums.append(line)
    for j in range(M):
        if line[j] == 1:
            queue.append([i,j,0])
#
def makeRipe(que):
    i,j,d = que
    if i>0 and nums[i-1][j]==0:
        nums[i-1][j] = 1
        queue.append([i-1,j,d+1])
    if j>0 and nums[i][j-1]==0:
        nums[i][j-1] = 1
        queue.append([i,j-1,d+1])
    if i<N-1 and nums[i+1][j]==0:
        nums[i+1][j] = 1
        queue.append([i+1,j,d+1])
    if j<M-1 and nums[i][j+1]==0:
        nums[i][j+1] = 1
        queue.append([i,j+1,d+1])
    return d
#
while(queue):
    que = queue.popleft()
    day = makeRipe(que)
#익지 못하는 토마토가 있는경우
for line in nums:
    for num in line:
        if(num == 0):
            print(-1)
            exit()
print(day)



#2178
import sys, collections
input = sys.stdin.readline
N,M = map(int,input().split())
graph,queue,visited = [], collections.deque([[0,0,1]]),[]
for _ in range(N):
    graph.append([int(s) for s in input().rstrip()])
def bfs(i,j,c):
    if(i<N-1 and graph[i+1][j] == 1):
        queue.append([i+1,j,c+1])
    if(j<M-1 and graph[i][j+1] == 1):
        queue.append([i,j+1,c+1])
    if(j>0 and graph[i][j-1] == 1):
        queue.append([i,j-1,c+1])
    if(i>0 and graph[i-1][j] == 1):
        queue.append([i-1,j,c+1])
while(queue):
    i,j,c = queue.popleft()
    if([i,j] in visited):
        continue
    if([i,j] == [N-1,M-1]):
        print(c)
        break
    visited.append([i,j])
    bfs(i,j,c)


#2146
import sys, collections
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())
graph,queue = [],collections.deque([])
for _ in range(N):
    graph.append([int(s) for s in input().split()])
#섬을 번호로 나누고 큐에 좌표추가
def makeIsland(i,j,n):
    graph[i][j] = [n,0]
    queue.append([i,j])
    if(i>0 and graph[i-1][j] == 1):
        makeIsland(i-1,j,n)
    if(j>0 and graph[i][j-1] == 1):
        makeIsland(i,j-1,n)
    if(i<N-1 and graph[i+1][j] == 1):
        makeIsland(i+1,j,n)
    if(j<N-1 and graph[i][j+1] == 1):
        makeIsland(i,j+1,n)
n=2
for i in range(N):
    for j in range(N):
        if(graph[i][j] == 1):
            makeIsland(i,j,n)
            n += 1

def expandIsland(i,j):
    n,d = graph[i][j]
    if(i>0 and graph[i-1][j] == 0):
        graph[i-1][j] = [n,d+1]
        queue.append([i-1,j])
    elif(i>0 and graph[i-1][j][0] != n):
        return graph[i-1][j][1]
    
    if(j>0 and graph[i][j-1] == 0):
        graph[i][j-1] = [n,d+1]
        queue.append([i,j-1])
    elif(j>0 and graph[i][j-1][0] != n):
        return graph[i][j-1][1]  
    
    if(i<N-1 and graph[i+1][j] == 0):
        graph[i+1][j] = [n,d+1]
        queue.append([i+1,j])
    elif(i<N-1 and graph[i+1][j][0] != n):
        return graph[i+1][j][1]
    
    if(j<N-1 and graph[i][j+1] == 0):
        graph[i][j+1] = [n,d+1]
        queue.append([i,j+1])
    elif(j<N-1 and graph[i][j+1][0] != n):
        return graph[i][j+1][1]
    return -1
output = 200
while(queue):
    i,j = queue.popleft()
    check = expandIsland(i,j)
    if(check != -1):
        output = min(output, check + graph[i][j][1])        
print(output)

#반례
# 1 0 0 0 1
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 1 1 0 0 1


#1991
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
graph = []
for _ in range(int(input())):
    v,l,r = input().split()
    graph.append(TreeNode(v,TreeNode(l),TreeNode(r)))

#트리완성
for i, node in enumerate(graph[:-1]):
    if(node.left.val != '.'):
        for next_node in graph[i+1:]:
            if(next_node.val == node.left.val):
                node.left = next_node
    if(node.right.val != '.'):
        for next_node in graph[i+1:]:
            if(next_node.val == node.right.val):
                node.right = next_node

def pre(root):
    global o1
    o1 += root.val
    if root.left.val != '.':
        pre(root.left)
    if root.right.val != '.':
        pre(root.right)
def mid(root):
    global o2
    if root.left.val != '.':
        mid(root.left)
    o2 += root.val
    if root.right.val != '.':
        mid(root.right)
def post(root):
    global o3
    if root.left.val != '.':
        post(root.left)    
    if root.right.val != '.':
        post(root.right)
    o3 += root.val

root,o1,o2,o3 = graph[0],'','',''
pre(root)
mid(root)
post(root)
print('\n'.join([o1,o2,o3]))


#11725
import sys, collections
input = sys.stdin.readline
N = int(input())
graph = collections.defaultdict(list)
for _ in range(N-1):
    k,v = map(int, input().split())
    graph[v].append(k)
    graph[k].append(v)

root,queue = [1] + [0] * (N-1), collections.deque([1])
while(queue):
    que = queue.popleft()
    for value in graph[que]:
        if not root[value-1]:
            queue.append(value)
            root[value-1] = que
print('\n'.join(map(str,root[1:])))            

# root,visited,queue = [0] * (N-1), [1] + [0] * N, collections.deque([1])
# while(queue):
#     que = queue.popleft()
#     for value in graph[que]:
#         if not visited[value-1]:
#             queue.append(value)
#             root[value-2] = que
#             visited[value-1] = 1
# print('\n'.join(map(str,root[])))


#1167
# 연결된점이 하나인곳에서만 시작하자. => 첫 정점에서 제일먼곳에서 다시 dfs한번하면 그게답이라고함.
# 나중에 다시풀자 ㅅ
import sys, collections
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
graph = collections.defaultdict(list)
V = int(input())
for _ in range(V):
    tmp = list(map(int,input().split()))[:-1]
    v = tmp[0]
    for i in range(1,len(tmp[1:]),2):
        graph[v].append([tmp[i],tmp[i+1]])
def dfs(key,before): 
    out,node = 0,0
    for value in graph[key]:
        if value[0] != before:
            tmp_out,tmp_node = dfs(value[0],key)
            tmp_out += value[1]
            if(tmp_out > out):
                out,node = tmp_out, tmp_node
        else:
            node = key
    return [out,node]
output,node = dfs(1,0)
output,node = dfs(node,0)
print(output)


#1967 아니 이건 맞는데 왜 위에껀 안맞는거야 씨빠업ㄹ야롬내ㅑ올ㄴ먀ㅐㅗ
import sys, collections
sys.setrecursionlimit(100000)
input = sys.stdin.readline
graph = collections.defaultdict(list)
for _ in range(int(input()) - 1):
    v1,v2,d = map(int,input().split())
    graph[v1].append([v2,d])
    graph[v2].append([v1,d])
def dfs(key,before):
    out,node = 0,0
    for value in graph[key]:
        if value[0] != before:
            tmp_out,tmp_node = dfs(value[0],key)
            tmp_out += value[1]
            if(tmp_out > out):
                out,node = tmp_out, tmp_node
        else:
            node = key
    return [out,node]
output,node = dfs(1,0)
output,node = dfs(node,0)
print(output)









