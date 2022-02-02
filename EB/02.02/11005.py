# 11005. 진법 변환2

import sys

system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = map(int, sys.stdin.readline().split())
rev_base = ''

while n != 0:
    rev_base += system[n % b]
    n = n // b

print(rev_base[::-1])
