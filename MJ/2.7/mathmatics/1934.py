# 8:35 -> 9:05
# 8:42 [Success]
import math

T = int(input())


def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


for _ in range(T):
    A, B = map(int, input().split())
    # print(math.lcm(A, B))
    print(A*B//gcd(A, B))
