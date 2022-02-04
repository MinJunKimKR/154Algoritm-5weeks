# 11653. 소인수분해

import sys

n = int(sys.stdin.readline())
i = 2

while i <= n:
    
    if n % i == 0:
        n //= i
        print(i)

    else:
        i += 1
