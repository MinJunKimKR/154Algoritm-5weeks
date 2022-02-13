#1963
#골드4

#4자리 소수
from collections import deque
import math
def get_prime_nums():
    prime = [True] * 10000
    prime[0], prime[1] = False, False
    
    for i in range(2, 10000):
        if prime[i] == True:
            j = 2

            while i * j < 10000:
                prime[i * j] = False
                j += 1
    #에라토스테네스의 체..
    return prime

n,m=map(int,input().split())

#뭔가 접근법은 bfs같은데..(전문제랑 비슷해보임 슈바)
#1,3,7,9

def bfs():
    queue=deque()
    queue.append([n,0])
    visited=[0 for x in range(10000)]
    cnt=0
    while(queue):
        x,cnt=queue.popleft()
        
        if x==m:
            print(cnt)
            return
        st=str(x)
        for i in range(4):
            for j in range(10):
                temp=int(st[:i]+str(j)+st[i+1:])
                
                if prime[temp] and visited[temp]==False and temp>=1000:
                    visited[temp]=1
                    queue.append([temp,cnt+1]) #cnt를 같이 넣어주는게 포인트..
    
    print('Impossible')
    
        
    
prime=get_prime_nums()
bfs()
