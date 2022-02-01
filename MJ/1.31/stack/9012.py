# 6:25 -> 6:55
# 6:50 [Success]
import sys
sys_input = sys.stdin.readline

N = int(input())

for _ in range(N):
    stack = []
    baskets = list(sys_input())
    for basket in baskets:
        if basket == '\n':
            continue

        if basket != '(':
            if len(stack) > 0 and stack[len(stack)-1] == '(':
                stack.pop()
            else:
                stack.append(basket)
        else:
            stack.append(basket)

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
