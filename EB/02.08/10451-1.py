# 10451. 순열 사이클- 코드 보충

def dfs(start):
    visited[start] = True
    next = arr[start]

    if not visited[next]:
        dfs(next)
        
    
import sys
sys.setrecursionlimit(10000) # Python 재귀 제한

input = sys.stdin.readline

for _ in range(int(input())):

    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)
    result = 0
    
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            result += 1

    print(result)
