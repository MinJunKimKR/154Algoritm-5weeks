#골드5
#2225


#점화식 찾기 힘들때는 표를 그려보자!
#점화식 : dp[i][j]=dp[i-1][j]+dp[i][j-1]
#k와 n의 관계를 찾는게 중요.

n, k = map(int, input().split())

dp = [[1]*(n + 1) for _ in range(k + 1)]
for i in range(1, k+1):
    dp[i][1] = i

for i in range(2,k+1):
    for j in range(2,n+1):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]

print(dp[k][n]%1000000000)

