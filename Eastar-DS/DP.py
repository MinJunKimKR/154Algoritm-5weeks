#1463
N = int(input())
def BPS(N):
    from collections import deque 
    queue = deque([[N,0]])
    solved = []
    while(queue):
        num, time = queue.popleft()
        if(num == 1):
            return time
        else:
            if(num%3 == 0 and num//3 not in solved):
                queue.append([num//3, time+1])
                solved.append(num//3)
            if(num%2 == 0 and num//2 not in solved):
                queue.append([num//2, time+1])
                solved.append(num//2)
            if(num-1 not in solved):
                queue.append([num-1, time+1])
                solved.append(num-1)
print(BPS(N))

#11726






















