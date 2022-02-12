#1931
#실버3

dic={}

n=int(input())
arr=list(map(int,input().split()))

arr.sort()

result=[]
sm=0
for i in arr:
    sm+=i
    result.append(sm)


print(sum(result))

    

