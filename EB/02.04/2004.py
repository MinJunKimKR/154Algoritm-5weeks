# 2004. 조합 0의 개수

import sys

def div_number(k, n):
    count = 0

    while k != 0:
        k = k // n
        count += k
        
    return count


n, m = map(int, sys.stdin.readline().split())

div_five = div_number(n, 5) - div_number(m, 5) - div_number(n-m, 5)
div_two = div_number(n, 2) - div_number(m, 2) - div_number(n-m, 2)

print(min(div_five, div_two))
