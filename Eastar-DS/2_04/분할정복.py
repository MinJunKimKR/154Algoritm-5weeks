# 분할정복

#11728
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
output = []
for _ in range(2):
    output += list(map(int,input().split()))
output.sort()
print(' '.join([str(num) for num in output]))

#1등풀이
import sys
input()
print(' '.join(sorted(sys.stdin.read().split(), key=int)))


#1780
import sys, collections
input = sys.stdin.readline
N = int(input())
nums = []
for _ in range(N):
    nums.append(input().split())
summ = [0,0,0]
def isSame(X,Y,n):
    s = nums[X][Y]
    for i in range(X,X+n):
        for j in range(Y,Y+n):
            if(nums[i][j] != s):
                for x in range(3):
                    for y in range(3):
                        isSame(X+n*x//3, Y+n*y//3, n//3)
                return            
    summ[int(s)] += 1
isSame(0,0,N)
print(f"{summ[-1]}\n{summ[0]}\n{summ[1]}\n")



#시간초과
def isSame(l,n):
    s = l[0][0]
    for i in range(n):
        for j in range(n):
            if(l[i][j] != s):
                for x in range(3):
                    for y in range(3):
                        isSame([ele[n*y//3:n*(y+1)//3] for ele in l[n*x//3:n*(x+1)//3]], n//3)
                return            
    summ[int(s)] += 1
isSame(nums,N)
print(f"{summ[-1]}\n{summ[0]}\n{summ[1]}\n")


#메모리초과
def isSameNum(l):
    start = l[0][0]
    for row in l:
        for ele in row:
            if(ele != start):
                return False
    return True
queue = collections.deque([nums])
while(queue):
    que = queue.popleft()
    if(isSameNum(que)):
        summ[int(que[0][0])] += 1
    else:
        length = len(que)
        for i in range(3):
            lines = [line for line in que[length*i//3:length*(i+1)//3]]
            for j in range(3):                
                queue.append([ele[length*j//3:length*(j+1)//3] for ele in lines])
print(f"{summ[-1]}\n{summ[0]}\n{summ[1]}\n")


#11729 풀이 죽이네...
N = int(input())
#n개를 1로 옮기는 함수
def hanoi(n,a,b,c):
    #a : 출발점 c : 도착점
    if(n==1):
        print(a,c)
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)
s=1
for _ in range(1,N):
    s = s*2 + 1
print(s)
hanoi(N,1,2,3)


#1992
import sys
input = sys.stdin.readline
N = int(input())
nums = [list(string for string in input()) for _ in range(N)]
output = []
def qud(X,Y,n):
    s = nums[X][Y]
    for x in range(X,X+n):
        for y in range(Y,Y+n):
            if(nums[x][y] != s):
                output.append('(')
                for i in range(2):
                    for j in range(2):
                        qud(X+i*n//2, Y+j*n//2, n//2)
                output.append(')')
                return
    output.append(s)
qud(0,0,N)
print(''.join(output))


#2447
N = int(input())
stars = [('* '*N).split() for _ in range(N)]
def paintStars(X,Y,n):
    for i in range(X + n//3,X + 2*n//3):
        for j in range(Y + n//3,Y + 2*n//3):
            stars[i][j] = ' '
    if(n>3):
        for i in range(3):
            for j in range(3):
                if([i,j] != [1,1]):
                    paintStars(X + i*n//3, Y + j*n//3, n//3)
paintStars(0,0,N)
for line in stars:
    print(''.join(line))


#2448
N = int(input())
def stars2448(n):
    if(n==3):
        stars,under = ['  *  ', ' * * ', '*****'],5
    else:
        stars,under = stars2448(n//2)[0],stars2448(n//2)[1]*2 + 1
        for i in range(len(stars)):
            stars.append(stars[i] + ' ' + stars[i])
        
        space = ((under-1)//2 + 1)//2
        for i in range(len(stars)//2):
            stars[i] = (' '*space) + stars[i] + (' '*space)
    return [stars,under]
stars = stars2448(N)[0]
for line in stars:
    print(line)


#1517 

#시간초과 난이도 보니 플래티넘이네 패스!
n = int(input())
nums = list(map(int,input().split()))
output = 0
for i in range(n-1):
    a = nums.pop()
    for j in range(n-1-i):
        if(nums[j] > a):
            output += 1
print(output)


#2261 아니 이건 무슨 플래2누?

























