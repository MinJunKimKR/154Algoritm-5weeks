# 9:43 -> 10:13
# 10:16 [Time out]
# 10:43
# 11:40 [Done ]
import sys
sys_input = sys.stdin.readline

left_stack = list(input())
right_stack = []
N = int(input())
cursor = len(left_stack)


for _ in range(N):
    command = sys_input()
    if command[0] == 'P':
        left_stack.append(command[2])
        continue
    if command[0] == 'L' and len(left_stack) > 0:
        right_stack.append(left_stack.pop())
        continue
    if command[0] == 'D' and len(right_stack) > 0:
        left_stack.append(right_stack.pop())
        continue
    if command[0] == 'B' and len(left_stack) > 0:
        left_stack.pop()
        continue

while len(right_stack) > 0:
    left_stack.append(right_stack.pop())

print(''.join(left_stack))
