# 10866. 덱

import sys
input = sys.stdin.readline

n = int(input())
deck = []

for i in range(n):

    st = input().split()
    order = st[0]

    if order == "push_front":
        deck.insert(0, int(st[1]))

    elif order == "push_back":
        deck.append(int(st[1]))

    elif order == "pop_front":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck.pop(0))

    elif order == "pop_back":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck.pop(-1))

    elif order == "size":
        print(len(deck))

    elif order == "empty":
        if len(deck) == 0:
            print(1)
        else:
            print(0)

    elif order == "front":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[0])
            
    elif order == "back":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[-1])
            
