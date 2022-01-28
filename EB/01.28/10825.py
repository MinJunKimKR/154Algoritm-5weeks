# 10825. 국영수

import sys
input = sys.stdin.readline

n = int(input())
student = []

for i in range(n):

    name, kor, eng, math = map(str, input().split())
    kor = int(kor)
    eng = int(eng)
    math = int(math)

    student.append([name, kor, eng, math])

result = sorted(student, key = lambda x: (-x[1], x[2], -x[3], x[0]))

for s in result:
    print(s[0])
