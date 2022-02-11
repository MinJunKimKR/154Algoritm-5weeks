#2447
#분할정복
#실버1

#전체모양을 가로로 3등분하여 문제해결.

import sys
sys.setrecursionlimit(100000000)
arr=[]

def sol(n):
    if n==1:
        return ['*']
    
    stars=sol(n//3)
    L=[]
    
    for s in stars:
        L.append(s*3)
    for s in stars:
        L.append(s+' '*(n//3)+s)
    for s in stars:
        L.append(s*3)   
    return L
    
    
n=int(input())
print('\n'.join(sol(n)))
    
