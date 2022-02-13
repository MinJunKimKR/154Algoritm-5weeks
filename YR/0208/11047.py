#11047
#실버3
#그리디


#거스름돈 문제와 접근방식이 동일한듯.


def sol(arr):
    global n,m
    global count
    
    for i in arr: #몫을 계산안하고 단순 while문으로 돌리면 시간초과남.
        if i<=m:
            mok=m//i
            m-=mok*i
            count+=mok
        
n,m=map(int,input().split())
arr=[]
count=0
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
sol(arr)
print(count)

    
