#11053
#가장 큰 증가 부분 수열
#실버 2
# dp는 점화식을 사용할수도 있지만 memoization을 사용할 수도 있음.
x=int(input())

arr = list(map(int, input().split()))

dp=[x for x in arr]

for i in range(x):
    for j in range(i):
        if arr[j]<arr[i]:
            dp[i]=max(dp[i],dp[j]+arr[i])
        

print(max(dp))
            

