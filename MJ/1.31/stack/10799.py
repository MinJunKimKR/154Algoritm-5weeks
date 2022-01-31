# 7:10 -> 7:40
# 7:31 [Success]
import sys
sys_input = sys.stdin.readline
stack = []
baskets = list(sys.stdin.readline())
pre = ''
stick_cnt = 0

for idx in range(0, len(baskets)-1):
    basket = baskets[idx]
    if basket == '(':
        stack.append(basket)
        pre = basket
        continue
    stack.pop()
    if pre == '(':
        # 레이저 발싸
        stick_cnt += len(stack)
    else:
        stick_cnt += 1
    pre = basket
print(stick_cnt)
