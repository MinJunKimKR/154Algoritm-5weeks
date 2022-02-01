#1912
#실버2

n=int(input())

arr = list(map(int, input().split()))
dp=[0 for x in range(n)]

dp[0]=arr[0]
for i in range(1,n):
    dp[i]=max(arr[i]+dp[i-1],arr[i])
    
print(max(dp))
        
    
