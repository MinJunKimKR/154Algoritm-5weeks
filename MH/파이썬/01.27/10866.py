#덱
import sys
input = sys.stdin.readline
n = int(input())
deck = []
for i in range(n):
    a = list(input().split())
    if a[0] == 'push_back':
        deck.append(a[1])
    elif a[0] == 'push_front':
        deck.insert(0,a[1])
    elif a[0] == 'front':
        if deck:
            print(deck[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if deck:
            print(deck[-1])
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(deck))
    elif a[0] == 'pop_front':
        if deck:
            print(deck.pop(0))
        else:
            print(-1)
    elif a[0] == 'pop_back':
        if deck:
            print(deck.pop())
        else:
            print(-1)
    elif a[0] == 'empty':
        if deck:
            print(0)
        else:
            print(1)

