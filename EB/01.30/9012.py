# 9012. 괄호 VPS

import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    ps = input()
    tmp = []

    for j in ps:
        if j == "(":
            tmp.append(j)

        elif j == ")":
            if len(tmp) != 0 and tmp[-1] == "(":
                tmp.pop()
            else:
                tmp.append(")")

    if len(tmp) == 0:
        print("YES")
    else:
        print("NO")
