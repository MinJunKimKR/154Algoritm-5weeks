n = int(input())
arr = [i for i in range(1,n+1)]

ans=1
for i in arr:
     ans*=i
print(ans)