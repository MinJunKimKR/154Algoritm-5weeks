# 9466. 텀 프로젝트

import sys
sys.setrecursionlimit(100000)   # 재귀로 인한 런타임 에러 방지
input = sys.stdin.readline

def dfs(start):
    global result
    
    visited[start] = True
    cycle.append(start)
    next = s[start]
    
    if visited[next]:   # 방문한 곳이라면
        if next in cycle:   # 사이클에 해당 인덱스 존재하는지
            result += cycle[cycle.index(next):] # 사이클이 되는 구간부터 팀을 이룸
            
        return
    
    else:   
        dfs(next)
        
for _ in range(int(input())):
    n = int(input())
    s = [0] + list((map(int, input().split())))
    # s.insert(0, 0)
    
    visited = [True] + [False] * n
    result = []
    
    for i in range(1, n+1):
        if not visited[i]:
            cycle = [] # 사이클 초기화
            dfs(i)
   
    print(n - len(result))
