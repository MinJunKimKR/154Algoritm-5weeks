#2331
#실버4

#dfs나 bfs는 아닌듯.
#어떤 탐색을 이용해야 하지?

#dfs였다..;;

#cnt를 세는 아이디어가 좀 어려웠다.!
import math

visited=[0 for i in range(250000)] 
s=[]


n,m=map(int,input().split())

def next(x,y):
    st=str(x)
    result=0
    for s in st:
        result+=pow(int(s),y) #pow는 제곱.
    return result


def dfs(v,cnt):
    if visited[v]!=0:
        return visited[v]-1
    
    visited[v]=cnt
    nxt=next(v,m)
    cnt+=1
    return dfs(nxt,cnt)


cnt=1
print(dfs(n,cnt))

