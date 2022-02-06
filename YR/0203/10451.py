#10451
#실버2


#입력받는 부분 처리만 다르고 지금까지 다뤘던 문제랑 같다.
#dfs
import sys
sys.setrecursionlimit(10000)

n=int(input())

for i in range(n):
    num=int(input())
    visit=[1]+[0 for i in range(num)] #방문 check 배열.
    s=[0]+list(map(int,input().split()))

    def dfs(v):
        visit[v]=1
        
        next=s[v] #다음 방문할 요소.
        if visit[next]==False:
            dfs(next)
        
        
    cnt=0
    for i in range(1,num+1):
        if visit[i]==False:
            dfs(i)
            cnt+=1 # 사이클 수 세기.

    print(cnt)
        
        
