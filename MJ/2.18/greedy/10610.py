# 9:27->9:57
# 10:01 [????]
N = list(input())

if N.count('0') == 0 or int(''.join(N)) < 30:
    print(-1)
    exit(0)
if sum(map(int, N)) % 3 != 0:
    print(-1)
    exit(0)

nums = sorted(N, reverse=True)
print(''.join(nums))
