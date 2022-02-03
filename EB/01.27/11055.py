# 11053. 가장 큰 증가 부분 수열

'''
n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n   # 0으로 초기화하면 안됨

dp[0] = arr[0]
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = dp[j] + arr[i]
print(dp)
print(max(dp))


'''
n = int(input())
arr = list(map(int, input().split()))
dp = [x for x in arr]

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))

