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


#10815 sys.stdin.readline
import time
start = time.time()
end = time.time()
print("time:", end-start)

import sys
N = int(input())
sang = sorted(list(map(int,input().split())))
sang += [sang[-1]+1]
M = int(input())
nums = list(map(int,input().split()))
output = ''

def bs(num):
    l,r = 0, N
    if(num<sang[l] or num>sang[r]-1):
        return False
    while(l < r-1):
        m = (l+r)//2
        if(num >= sang[m]):
            l = m
        else:
            r = m
    if(sang[l] == num):
        return True
    else:
        return False
    
for num in nums:    
    if bs(num):
        output += '1 '
    else:
        output += '0 '
print(output[:-1])


#빠른풀이 ㄷㄷ; set하나에 나는 안되고 얘는 된다고?
import sys
input = sys.stdin.readline
def Test():
    n,tmp,m = input(),set(input().split()),input()
    res = ""
    for i in input().split():
        if i in tmp:
            res +="1 "
        else:
            res +="0 "
    print(res)
Test()


#시간초과
import sys
N = int(input())
sang = sorted(list(map(int,input().split())))
M = int(input())
nums = list(map(int,input().split()))
output = ''
for num in nums:
    if(num in sang):
        output += '1 '
    else:
        output += '0 '
print(output[:-1])



#10816
import sys
input = sys.stdin.readline    
import collections
N = int(input())
nums1 = input().split()
M = int(input())
nums2 = input().split()
counter = collections.Counter(nums1)
print(' '.join(f'{counter[m]}' if m in counter else '0' for m in nums2))

#시간초과
N = int(input())
nums1 = input().split()
M = int(input())
nums2 = input().split()
output = [0]*M
for num in nums1:
    try:
        output[nums2.index(num)] += 1
    except:
        pass
print(' '.join([str(n) for n in output]))



#11662 삼분탐색을 공부했다.
import sys
input = sys.stdin.readline
ax,ay,bx,by,cx,cy,dx,dy = map(int,input().split())
l,r = 0,1
while((r-l)>0.00000001):
    ll,rr = l+(r-l)/3, l+(r-l)/1.5
    d1,d2 = (((ax+(bx-ax)/3) - (cx+(dx-cx)/3))**2 + ((ay+(by-ay)/3) - (cy+(dy-cy)/3))**2)**0.5, (((ax+(bx-ax)/1.5) - (cx+(dx-cx)/1.5))**2 + ((ay+(by-ay)/1.5) - (cy+(dy-cy)/1.5))**2)**0.5
    if(d1 >= d2):
        l = ll
        ax,ay,cx,cy = ax+(bx-ax)/3, ay+(by-ay)/3, cx+(dx-cx)/3, cy+(dy-cy)/3
    else:
        r = rr
        bx,by,dx,dy = ax+(bx-ax)/1.5, ay+(by-ay)/1.5, cx+(dx-cx)/1.5, cy+(dy-cy)/1.5
print(d1)






















