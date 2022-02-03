# 10814. 나이순 정렬

import sys
input = sys.stdin.readline

n = int(input())
member = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    member.append([i, age, name])

result = sorted(member, key = lambda x: (x[1], x[0]))

for i in result:
    print(i[1], i[2])
