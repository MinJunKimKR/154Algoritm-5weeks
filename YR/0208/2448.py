#2447
#분할정복
#골드4


import sys
sys.setrecursionlimit(100000000)
arr=[]

def sol(n):
    if n==3:
        return ['  *  ',' * * ','*****']
    
    stars=sol(n//2)
    L=[]
    for s in stars:
        L.append(' '*(n//2)+s+' '*(n//2))
    for s in stars:
        L.append(s+' '+s)   
    return L
    
n=int(input())
print('\n'.join(sol(n)))
    
