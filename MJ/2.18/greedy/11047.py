# 9:12 -> 9:42
# 9:17[success]
N, K = map(int, input().split())
coins = []
cnt_coin = 0
for _ in range(N):
    coins.append(int(input()))


for i in range(N-1, -1, -1):
    coin = coins[i]
    if coin > K:
        continue
    cnt_coin += K//coin
    K = K % coin

print(cnt_coin)
