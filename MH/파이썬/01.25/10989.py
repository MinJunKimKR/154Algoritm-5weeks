#수 정렬하기 3

import sys
input = sys.stdin.readline
n = int(input())
arr = [0]*10000
for i in range(n):
    num = int(input())
    arr[num-1]+=1
for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)

