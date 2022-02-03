# 2751. 수 정렬하기2

'''
# 시간 초과 
n = int(input())    # Test case
a = [0] * n

for i in range(n):
    a[i] = int(sys.stdin.readline())

for i in range(n):
    for j in range(i):
        if a[j] > a[i]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
            
for i in range(n):
    print(a[i])
'''

import sys

n = int(input())
a = []

for i in range(n):
    a.append(int(sys.stdin.readline()))
for i in sorted(a):
    sys.stdout.write(str(i) + "\n")
