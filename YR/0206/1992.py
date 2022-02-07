#1992
#분할정복
#실버1

import sys
sys.setrecursionlimit(100000000)
arr=[]

def sol(n,x,y):
    chk=arr[x][y]
    #2*2 크기 일때 예외처리를 안해도 되는이유는 머지?
    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j]!=chk:
                print('(',end='')
                for k in range(2):
                    for l in range(2):
                        sol(n//2,x+k*n//2,y+l*n//2)
                print(')',end='')
                return
    
    if chk==0:
        print('0',end='')
    elif chk==1:
        print('1',end='')
    
    
n=int(input())
for i in range(n):
    arr.append(list(map(int,input())))

sol(n,0,0)
    
