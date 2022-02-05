# 1929. 소수 구하기

import sys

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                return False
        return True


m, n = map(int, sys.stdin.readline().split())

for i in range(m, n+1):
    if isPrime(i):
        print(i)

'''
시간 초과
import sys

m, n  = map(int, sys.stdin.readline().split())


for i in range(m, n+1):
    sum = 0

    for j in range(1, i):
        if i % j == 0:
            sum += 1
    if sum == 1:
        print(i)
'''
