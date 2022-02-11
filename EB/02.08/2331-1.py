# 2331. 반복 수열 - 보충

import sys

a, p = map(int, sys.stdin.readline().split())
seq = [a]

while True:
    t = seq[-1]
    val = 0

    while t:
        val += ((t%10) ** p)
        t //= 10

    if val in seq:
        print(seq.index(val))   # count하지 않고 해당 정수 index 출력
        break
    else:
        seq.append(val)
