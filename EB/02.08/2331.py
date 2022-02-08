# 2331. 반복 수열

import sys

a, p = map(str, sys.stdin.readline().split())
D = ['0', a]

idx = 2
result = 0
while True:
    result = 0

    for a in D[idx-1]:
       result += (int(a)**int(p))

    D.append(str(result))

    if D.count(str(result)) != 1:
        break

    idx += 1
    

n = D[idx]
count = 0
for i in range(1, len(D)):
    if D[i] == n:
        break
    count += 1

print(count)
