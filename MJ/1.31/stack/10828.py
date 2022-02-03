# 6:10 -> 6:40
# 6:19 [Success]
import sys
sys_input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    command = sys_input().split()
    if command[0] == 'push':
        stack.append(command[1])
        continue
    if command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
        continue
    if command[0] == 'size':
        print(len(stack))
        continue
    if command[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
        continue
    if command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
        continue
