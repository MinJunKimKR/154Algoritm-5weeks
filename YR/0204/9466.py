#9466
#골드3

#이건 누가봐도 dfs or bfs.
#cycle을 이루냐 안이루냐를 판단하는 과정이 어려웠음..ㅜㅜ
import sys
sys.setrecursionlimit(1000000)

number=int(input())
for _ in range(number):
    n=int(input())

    s=[0]+list(map(int,input().split()))
    visited=[1]+[0 for x in range(n+1)]
    result=[]


    def dfs(v):
        global result
        visited[v]=1
        cycle.append(v) 
        
        next=s[v]
        if visited[next]==False:
            dfs(next)
        else:
            if next in cycle: #사이클 가능 여부.
                result+=cycle[cycle.index(next):] #index(x) 함수는 리스트에 x 값이 있으면 x의 위치 값을 돌려준다.
            return
        
        
    cnt=0
    for i in range(1,n+1):
        if visited[i]==False:
            cycle=[]
            dfs(i)
            
            
    print(n-len(result))




    
