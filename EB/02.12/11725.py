# 11725. 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)] # [] 1 ~ n
parents = [0 for _ in range(n+1)]

for _ in range(1, n):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(start):
    for i in tree[start]:
        
        if parents[i] == 0:
            parents[i] = start
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(parents[i])
