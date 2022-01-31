#1699
#실버3
#bottom up memoization?

#제곱수를 작은 수부터 대입해 나가는 문제!

n=int(input())

dp=[x for x in range(n+1)]

for i in range(1,n+1):
    for j in range(1,i): #j는 제곱수.
        if j*j>i:
            break
            
        if dp[i-j*j]+1<dp[i]:
            dp[i]=dp[i-j*j]+1
            


print(dp[n])

