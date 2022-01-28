#2579
#실버3
#점화식을 세우는 문제였음..!
#3번 연속 계단을 밟을 수 없기 때문에 그에 따른 조건에 따른 식 세우기

n=int(input())
arr=[0 for i in range(301)]
dp=[0 for i in range(301)]
for i in range(n):
    arr[i]=(int(input()))
    
dp[0]=(arr[0])
dp[1]=(arr[1]+arr[0])
dp[2]=(max(arr[0]+arr[2],arr[1]+arr[2]))

for i in range(3,n):
    dp[i]=(max(arr[i]+arr[i-1]+dp[i-3],arr[i]+dp[i-2]))
    
print(dp[n-1])



