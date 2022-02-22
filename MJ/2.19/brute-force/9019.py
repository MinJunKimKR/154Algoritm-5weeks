# 9:15 -> 9:55
# 10:02 [Fail - timeout]
# refer : https://paris-in-the-rain.tistory.com/94

import sys
from collections import deque

# D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.


def oper_D(n):
    res = n * 2
    if res > 9999:
        res %= 10000
    return res

# S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.


def oper_S(n):
    res = n
    if res == 0:
        return 9999
    res -= 1
    return res


def oper_L(n):  # 왼쪽으로 회전 : 1234 -> 2341
    front = n % 1000
    back = n // 1000
    res = front*10 + back
    return res


def oper_R(n):  # 오른쪽으로 회전 : 1234 -> 4123
    front = n % 10
    back = n // 10
    res = front*1000 + back
    return res


def go(s, t):
    queue = deque()
    visited = set()  # logn
    queue.append((s, ""))
    visited.add(s)
    while queue:
        cur_num, oper = queue.popleft()
        if cur_num == t:
            print(oper)
            return
        tmp = oper_D(cur_num)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, oper+"D"))

        tmp = oper_S(cur_num)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, oper+"S"))

        tmp = oper_L(cur_num)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, oper+"L"))

        tmp = oper_R(cur_num)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, oper+"R"))


for _ in range(int(input())):
    start, target = map(int, input().split())
    # print(start, target)
    go(start, target)
