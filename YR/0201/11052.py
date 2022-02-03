#11052
#실버1

n=int(int(input()))

arr=[0]+list(map(int,input().split()))

dp=[0 for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i]=max(dp[i],dp[i-j]+arr[j])
    
#dp[1]=arr[1]
#dp[2]=arr[2]+dp[0]
#dp[3]=arr[3]+dp[0], arr[2]+dp[1], arr[1]+dp[2] ,,,

print(dp[n])
