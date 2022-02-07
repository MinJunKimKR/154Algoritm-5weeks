# 1934. 최소 공배수

import sys
import math

t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(math.lcm(a, b))
'''
import sys

t = int(sys.stdin.readline())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))
'''
