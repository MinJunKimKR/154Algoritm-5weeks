# 10:04 -> 10:34
# 10:32 [Fail]
# 10:44 [문제이해를 잘못함]
N, M = map(int, input().split())
if N == 1 or M == 1:
    print(1)
    exit(0)
if N == 2:
    print(min(4, 1+((M-1)//2)))
    exit(0)

if M < 7:
    print(min(4, M))
    exit(0)
print(M-2)
