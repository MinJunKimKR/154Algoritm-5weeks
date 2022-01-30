# 10828. 스택

import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    str = input().split()
    order = str[0]
    
    if order == "push":
        stack.append(str[1])

    elif order == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
            
    elif order == "size":
        print(len(stack))
        
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
    elif order == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

'''
n = int(input())
stack = []

for i in range(n):

    str = input()
    
    if str.find("push") != -1:
        a, b = str.split()
        b = int(b)
        stack.append(b)

    elif str.find("pop") != -1:
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop())
        
    elif str.find("size") != -1:
        print(len(stack))

    elif str.find("empty") != -1:
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    elif str.find("top") != -1:
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[len(stack)-1])

'''
