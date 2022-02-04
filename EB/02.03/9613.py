# 9613. GCD 합

import sys
import math

t = int(sys.stdin.readline())
result = []

for i in range(t):
    s = sys.stdin.readline().split()    # list(map(int, sys.stdin.readline().split()))
    n = int(s[0])
    result.clear()
    
    for j in range(1, n+1):
        result.append(int(s[j]))

    sum = 0
    for j in range(len(result)):
        for k in range(j):
            sum += math.gcd(result[j], result[k])

    print(sum)   



