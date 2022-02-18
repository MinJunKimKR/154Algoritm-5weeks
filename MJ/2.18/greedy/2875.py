# 9:18 -> 9:48
# 9:26[SUCCESS]
N, M, K = map(int, input().split())


for _ in range(K):
    if N > M*2:
        N -= 1
        # continue
    else:
        M -= 1

if N > M*2:
    print(M)
else:
    print(N//2)
