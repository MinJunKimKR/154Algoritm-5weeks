# 10845. 큐

import sys
input = sys.stdin.readline

n = int(input())
queueList = []


for _ in range(n):

    inputData = input().split()
    order = inputData[0]

    if order == "push":
        data = int(inputData[1])
        queueList.append(data)
        
    elif order == "pop":
        if len(queueList) == 0:
            print(-1)
        else:
            print(queueList.pop(0))
            
    elif order == "size":
        print(len(queueList))
        
    elif order == "empty":
        if len(queueList) == 0:
            print(1)
        else:
            print(0)
            
    elif order == "front":
        if len(queueList) == 0:
            print(-1)
        else:
            print(queueList[0])
            
    elif order == "back":
        if len(queueList) == 0:
            print(-1)
        else:
            print(queueList[-1])
