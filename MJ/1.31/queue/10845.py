# 7:37 -> 8:07
# 7:49 [Success]
import sys
from collections import deque
sys_input = sys.stdin.readline

N = int(input())
q = deque([])

for _ in range(N):
    command = sys_input().split()
    if command[0] == 'push':
        q.append(int(command[1]))
        continue
    if command[0] == 'pop':
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
        continue
    if command[0] == 'size':
        print(len(q))
        continue
    if command[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
        continue
    if command[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
        continue
    if command[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[len(q)-1])
        continue
