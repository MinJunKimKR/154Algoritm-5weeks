#Stack, Queue, Deck

#10828
import sys
N = int(sys.stdin.readline())
stack = []
def push(X):
    stack.append(X)
def pop():
    if(stack):
        print(stack.pop())
    else:
        print(-1)
def size():
    print(len(stack))
def empty():
    print(int(not bool(stack)))
def top():
    if(stack):
        print(stack[-1])
    else:
        print(-1)

for i in range(N):
    order = sys.stdin.readline().split()
    if(order[0] == 'push'):
        push(int(order[1]))
    elif(order[0] == 'pop'):
        pop()
    elif(order[0] == 'size'):
        size()
    elif(order[0] == 'empty'):
        empty()
    elif(order[0] == 'top'):
        top()


#9012 input하고 sys하고 차이를 정확히 알게해준 문제.
import sys
N = int(sys.stdin.readline())
def isVPS(ps):    
    stack = []
    if(len(ps)%2 == 1):        
        return print('NO')
    for p in ps:
        if(p == '('):
            stack.append(p)
        else:
            if(stack):
                stack.pop()
            else:                
                return print('NO')
    if(stack):
        return print('NO')
    else:
        return print('YES')
for _ in range(N):
    ps = sys.stdin.readline()
    isVPS(ps[:-1])


#10799
#뒤괄호보고 레이저판단
#레이저면 막대개수만큼 + 레이저아니면 막대시작이면 +1 막대끝이면 막대빼주기
ps = input()
stack, laser, output = [], 0, 0
for i,p in enumerate(ps):
    #앞선 검사에서 뒷괄호를 빼줘야한다고 기록해줬으면 빼주기.
    if(laser):
        laser = 0
        continue
    if(p=='('):
        #레이저면 막대개수만큼 더하고 뒷괄호 빼줄준비.
        if(ps[i+1] == ')'):
            output += len(stack)
            laser = 1
        #막대 시작이면
        else:
            output += 1
            stack.append(1)
    else:
        stack.pop()
print(output)

#스택을 숫자로 변경해서 좀더빠르고 메모리 좀더적음
ps = input()
stack, laser, output = 0, 0, 0
for i,p in enumerate(ps):
    #앞선 검사에서 뒷괄호를 빼줘야한다고 기록해줬으면 빼주기.
    if(laser):
        laser = 0
        continue
    if(p=='('):
        #레이저면 막대개수만큼 더하고 뒷괄호 빼줄준비.
        if(ps[i+1] == ')'):
            output += stack
            laser = 1
        #막대 시작이면
        else:
            output += 1
            stack += 1
    else:
        stack -= 1
print(output)


#10845
import sys,collections
N = int(sys.stdin.readline())
queue = collections.deque([])
def push(X):
    queue.append(X)
def pop():
    if(queue):
        print(queue.popleft())
    else:
        print(-1)
def size():
    print(len(queue))
def empty():
    print(int(not bool(queue)))
def front():
    if(queue):
        print(queue[0])
    else:
        print(-1)
def back():
    if(queue):
        print(queue[-1])
    else:
        print(-1)

for _ in range(N):
    order = sys.stdin.readline().split()
    if(order[0] == 'push'):
        push(int(order[1]))
    elif(order[0] == 'pop'):
        pop()
    elif(order[0] == 'size'):
        size()
    elif(order[0] == 'empty'):
        empty()
    elif(order[0] == 'front'):
        front()
    elif(order[0] == 'back'):
        back()

#10866
import sys,collections
N = int(sys.stdin.readline())
queue = collections.deque([])
def push_front(X):
    queue.appendleft(X)
def push_back(X):
    queue.append(X)
def pop_front():
    if(queue):
        print(queue.popleft())
    else:
        print(-1)
def pop_back():
    if(queue):
        print(queue.pop())
    else:
        print(-1)
def size():
    print(len(queue))
def empty():
    print(int(not bool(queue)))
def front():
    if(queue):
        print(queue[0])
    else:
        print(-1)
def back():
    if(queue):
        print(queue[-1])
    else:
        print(-1)

for _ in range(N):
    order = sys.stdin.readline().split()
    if(order[0] == 'push_back'):
        push_back(int(order[1]))
    elif(order[0] == 'push_front'):
        push_front(int(order[1]))
    elif(order[0] == 'pop_back'):
        pop_back()
    elif(order[0] == 'pop_front'):
        pop_front()
    elif(order[0] == 'size'):
        size()
    elif(order[0] == 'empty'):
        empty()
    elif(order[0] == 'front'):
        front()
    elif(order[0] == 'back'):
        back()






























