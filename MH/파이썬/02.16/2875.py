n,m,k = map(int,input().split())
result = 0

while n>=2 and m>= 1 and n+m>=k+3:
    n-=2
    m-=1
    result+=1
print(result)