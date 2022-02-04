# 2609. 최대 공약수와 최소 공배수

import sys

a, b = map(int, sys.stdin.readline().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))

'''
python 라이브러리 사용 3.9 이상 가능
import sys
import math

a, b = map(int, sys.stdin.readline().split())

print(math.gcd(a, b))
print(math.lcm(a, b))
'''
