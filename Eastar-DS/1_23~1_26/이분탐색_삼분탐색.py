#이분탐색/삼분탐색 

#1654 sys.stdin.readline
import math
K,N = map(int,input().split())
L = []
for _ in range(K):
    l = int(input())
    L.append(l)
l,r = 1 , max(L)
while(l < r):    
    m = math.floor(r/2 + l/2)
    n = sum([num//m for num in L])
    if(n<N):
        r = m
    else:
        l = m
    if(l==(r-1)):
        if(sum([num//r for num in L]) >= N):
            l = r
        break
print(l)


import math,sys
K,N = map(int,sys.stdin.readline().split())
L = []
for _ in range(K):
    l = int(sys.stdin.readline())
    L.append(l)
l,r = 1 , max(L)
while(l < r):    
    m = math.floor(r/2 + l/2)
    n = sum([num//m for num in L])
    if(n<N):
        r = m
    else:
        l = m
    if(l==(r-1)):
        if(sum([num//r for num in L]) >= N):
            l = r
        break
print(l)




































