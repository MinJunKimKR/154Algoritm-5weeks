#5:40 -> 6:20
# 5:54 [GG]
# refer :https://br-brg.tistory.com/18
# 6:40 -> 7:30[Success]
N, K = map(int,input().split())
MOD = 1000000000
dp = [[0]*(N+1) for _ in range(K+1)]

for n in range(1, N+1):
    dp[1][n] = 1

for k in range(2,K+1):
    for n in range(1,N+1):
        total = 1
        for i in range(1,n+1):
            total += dp[k-1][i]
        dp[k][n] = total
        
print(dp[K][N] % MOD)