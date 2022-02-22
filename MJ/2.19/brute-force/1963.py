# 5:18 -> 5:58
# 5:55 [Success]
from collections import deque
import sys
sys_input = sys.stdin.readline
T = int(input())


def eratos(len):
    sosu = [True]*(len+1)
    sosu[0] = sosu[1] = False
    for i in range(2, len+1):
        if sosu[i]:
            idx = i+i
            while idx <= len:
                sosu[idx] = False
                idx = idx+i
    return sosu


sosu = eratos(9999)

for _ in range(T):
    start, end = sys_input().strip().split()
    visited = [0]*10000
    queue = deque([start])
    is_not_find = True
    while queue:
        password = queue.popleft()
        if password == end:
            print(visited[int(password)])
            is_not_find = False
            break
        arr_password = list(password)
        for i in range(4):
            for j in range(10):
                new_password = int(
                    ''.join(arr_password[:i]+[str(j)]+arr_password[i+1:]))
                if new_password < 1000:
                    continue
                if visited[new_password] == 0 and sosu[new_password] and new_password != int(start):
                    visited[new_password] = visited[int(password)]+1
                    queue.append(str(new_password))
    if is_not_find:
        print('Impossible')
