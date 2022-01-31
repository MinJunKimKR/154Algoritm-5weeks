# 12:21 -> 12:51
# 12:31 [SUCCESS]
from collections import deque
import sys
sys_input = sys.stdin.readline
deck = deque([])

N = int(input())

for _ in range(N):
    command = sys_input().split()
    if command[0] == 'push_front':
        deck.appendleft(command[1])
        continue
    if command[0] == 'push_back':
        deck.append(command[1])
        continue
    if command[0] == 'pop_front':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck.popleft())
        continue
    if command[0] == 'pop_back':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck.pop())
        continue
    if command[0] == 'size':
        print(len(deck))
        continue
    if command[0] == 'empty':
        if len(deck) == 0:
            print(1)
        else:
            print(0)
        continue
    if command[0] == 'front':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[0])
        continue
    if command[0] == 'back':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[len(deck)-1])
        continue
