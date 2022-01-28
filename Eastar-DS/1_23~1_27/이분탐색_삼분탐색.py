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


#2805
import sys,math
N,M = map(int,input().split())
trees = list(map(int,input().split()))
l,r = 0,max(trees)
while(l<r):
    m = math.floor(r/2+l/2)
    summ = sum([num-m for num in trees if num > m])
    if(summ >= M):
        l = m
    else:
        r = m
    if(l == (r-1)):
        break
print(l)
    

import sys,math
N,M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))
l,r = 0,max(trees)
while(l<r):
    m = math.floor(r/2+l/2)
    summ = sum([num-m for num in trees if num > m])
    if(summ >= M):
        l = m
    else:
        r = m
    if(l == (r-1)):
        break
print(l)


#2110
import sys
N,C = map(int,input().split())
home = []
for _ in range(N):
    home.append(int(input()))
home.sort()
l,r = 1,(home[0]+home[-1])//(C-1) + 1
while(l<r):
    now,length = home[0],1
    m = (l+r)//2
    for h in home[1:]:
        if(h >= now+m):
            length += 1
            now = h
        if(length == C):
            l = m
            break
    if(length >= C):
        l = m
    else:
        r = m
    if(l == r-1):
        break
print(l)


import sys
N,C = map(int,sys.stdin.readline().split())
home = []
for _ in range(N):
    home.append(int(sys.stdin.readline()))
home.sort()
l,r = 1,(home[0]+home[-1])//(C-1) + 1
while(l<r):
    now,length = home[0],1
    m = (l+r)//2
    for h in home[1:]:
        if(h >= now+m):
            length += 1
            now = h
        if(length == C):
            l = m
            break
    if(length >= C):
        l = m
    else:
        r = m
    if(l == r-1):
        break
print(l)






















