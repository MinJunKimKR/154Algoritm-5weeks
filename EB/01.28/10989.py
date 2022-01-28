# 10989. 수 정렬하기3

import sys
input = sys.stdin.readline

n = int(input())

'''
메모리 초과..
a = []

for i in range(n):
    a.append(int(input()))

a.sort()

for i in a:
    print(i)
'''

b = [0] * 10001

for i in range(n):
    b[int(input())] += 1

for i in range(10001):
    if b[i] != 0:
        for _ in range(b[i]):
            print(i)
