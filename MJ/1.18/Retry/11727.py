# 4:45 -> 5:15
# 4:50 [runtime error] - 초기 배열 선언 크기 문제 (엣지케이스 = 1)
# 4:57 [Success]
N = int(input())
mod = 10007
dp = [0]*(1001)
dp[1], dp[2] = 1,3

for i in range(3,N+1):
    dp[i] = dp[i-1] + (2*dp[i-2])
    
print(dp[N]%mod) 
        