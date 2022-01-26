#수 정렬하기 3

import sys
input = sys.stdin.readline
num = int(input())
arr = [0]*10000

for i in range(num):
    a = int(input())
    arr[a-1] += 1

for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)