from collections import deque

num = int(input())

arr = [[] for _ in range(num+1)]

for _ in range(num-1):
    a,b,c = map(int,input().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

def bfs(i):
    check = [-1]*(num+1)
    check[i] = 0
    q = deque()
    q.append(i)
    _max = [0,0]
    while q:
        x = q.popleft()
        for a,b in arr[x]:
            if check[a] == -1:
                check[a] = check[x]+b
                q.append(a)
                if _max[1] < check[a]:
                    _max = a,check[a]
    return _max


node,dist = bfs(1)
node,dist = bfs(node)
print(dist)
