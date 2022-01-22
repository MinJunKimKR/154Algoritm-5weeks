#실버1
#10844와 유사해보임.
#dp 문제는 점화식과 규칙을 찾는것이 중요!

n=int(input())

dp = [[0 for _ in range(10)] for _ in range(n+1)]
for i in range(10):
    dp[1][i] = 1

for i in range(2,n+1):
    for j in range(10):
        for k in range(j+1):
            dp[i][j]+=dp[i-1][k]
#j가 마지막 글자. 오름차순이므로 앞의것들이 dp[i][0]..dp[i][j]까지 올수 있음.

print(sum(dp[n])%10007)
