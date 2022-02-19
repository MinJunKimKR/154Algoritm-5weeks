#완전탐색

#1476
e,s,m = map(int,input().split())
while(e!=s or s!=m):
    if(e<=s and e<=m):
        e+=15
    elif(s<=e and s<=m):
        s+=28
    else:
        m+=19
print(e)


#1107 내가 진짜 찾고싶었던 기능을 이문제덕에 찾았네
N = int(input())
M = int(input())
if(not M):
    print(min(abs(N-100), len(str(N))))
else:
    broken = input().split()
    #+ - 로만 이동한값
    output = abs(N-100)
    #50만을 9로만 표현하면 99999에서 올라오는게 빠르므로 888888까지만 확인하면됨. 
    #범위에 대한걸 나중에 더 줄일 수 있을듯.
    for num in range(888889):
        for n in str(num):
            if n in broken:
                break
        else:
            output = min(output, abs(num-N) + len(str(num)))
    print(output)


#1451
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
nums = []
for _ in range(N):
    nums.append(list(map(int,list(input()))))
output = 0
if(N == 1):
    for i in range(M-2):
        for j in range(i+1,M-1):
            output = max(output, sum(nums[0][:i+1])*sum(nums[0][i+1:j+1])*sum(nums[0][j+1:]))
elif(M == 1):
    for i in range(N-2):
        for j in range(i+1,N-1):
            a,b,c = 0,0,0
            for k in range(N):
                if(k<=i):
                    a += nums[k][0]
                elif(i<k<=j):
                    b += nums[k][0]
                else:
                    c += nums[k][0]
            output = max(output, a*b*c)
else:
    #한점에서 십자가로 자르고 3개의 직사각형을 만들어 구하자.
    for x in range(1,N):
        for y in range(1,M):            
            #위의 두사각형합치면
            a,b,c = 0,0,0
            for i in range(x):
                a += sum(nums[i])
            for i in range(x,N):
                for j in range(y):
                    b += nums[i][j]
                for j in range(y,M):
                    c += nums[i][j]
            output = max(output, a*b*c)            
            #아래 두사각형합치면
            a,b,c = 0,0,0
            for i in range(x):
                for j in range(y):
                    b += nums[i][j]
                for j in range(y,M):
                    c += nums[i][j]            
            for i in range(x,N):
                a += sum(nums[i])
            output = max(output, a*b*c)
            #왼쪽 두사각형 합치면
            a,b,c = 0,0,0
            for i in range(N):
                for j in range(M):
                    if(j<y):
                        a += nums[i][j]
                    else:
                        if(i<x):
                            b += nums[i][j]
                        else:
                            c += nums[i][j]
            output = max(output, a*b*c)            
            #오른쪽
            a,b,c = 0,0,0
            for i in range(N):
                for j in range(M):
                    if(j>=y):
                        a += nums[i][j]
                    else:
                        if(i<x):
                            b += nums[i][j]
                        else:
                            c += nums[i][j]
            output = max(output, a*b*c)
    #평행하게 가로로 자를때
    for x in range(1,N-1):
        for y in range(x+1,N):
            a,b,c = 0,0,0
            for i in range(N):
                if(i<x):
                    a += sum(nums[i])
                elif(i<y):
                    b += sum(nums[i])
                else:
                    c += sum(nums[i])
            output = max(output, a*b*c)
    #평행하게 세로로 자를때
    for x in range(1,M-1):
        for y in range(x+1,M):
            a,b,c = 0,0,0
            for i in range(N):
                for j in range(M):
                    if(j<x):
                        a += nums[i][j]
                    elif(j<y):
                        b += nums[i][j]
                    else:
                        c += nums[i][j]
            output = max(output, a*b*c)
print(output)


#10819
N = int(input())
nums = list(map(int,input().split()))
nums.sort()
output = 0
#큰거양쪽에넣고 작은거양쪽에넣고 반복하면 최대가됨. 혹은 그반대.
if(N%2 == 1):
    nums1,nums2 = [nums[0]],[nums[N-1]]
    i,j = 1,N-1
    while(i<j):
        nums1 = [nums[j-1]] + nums1 + [nums[j]]
        j -= 2
        if(i<j):
            nums1 = [nums[i+1]] + nums1 + [nums[i]]
            i += 2
    i,j = 0,N-2
    while(i<j):
        nums2 = [nums[i+1]] + nums2 + [nums[i]]
        i +=2
        if(i<j):
            nums2 = [nums[j-1]] + nums2 + [nums[j]]
            j-=2
        
    output1, output2 = 0,0
    for i in range(N-1):
        output1 += abs(nums1[i]-nums1[i+1])
        output2 += abs(nums2[i]-nums2[i+1])
    print(max(output1,output2))
else:
    nums1 = [nums[0]]
    i,j = 1,N-1
    while(i<j):
        nums1 = [nums[j-1]] + nums1 + [nums[j]]
        j -= 2
        if(i<j):
            nums1 = [nums[i+1]] + nums1 + [nums[i]]
            i += 2
    nums1,nums2 = (nums1 + [nums[i]]), ([nums[i]] + nums1)
    output1, output2 = 0,0
    for i in range(N-1):
        output1 += abs(nums1[i]-nums1[i+1])
        output2 += abs(nums2[i]-nums2[i+1])
    print(max(output1,output2))
    
    
    
#10971
import time
#백트래킹 조건으로 tmp > output인걸 생각해내야함.
import itertools
N = int(input())
cost = [[int(string) for string in input().split()] for _ in range(N)]
#진짜 아슬하게통과
start = time.time()

per = itertools.permutations([i for i in range(N)],N)
output = 10000000
for p in per:
    tmp = 0
    for i, v in enumerate(p,-1):
        if(cost[p[i]][v] == 0 or output <= tmp):
            break
        tmp += cost[p[i]][v]
    else:
        output = min(tmp,output)
print(output)

end = time.time()
print(end-start)


#1697
import collections
n,k = map(int,input().split())
queue,visited = collections.deque([[n,0]]),[0]*100001
while(queue):
    n,c = queue.popleft()
    if(visited[n] == 1):
        continue
    if(n == k):
        print(c)
        break
    visited[n] = 1
    if(n>0):
        queue.append([n-1,c+1])
    if(n<100000):
        queue.append([n+1,c+1])
    if(2*n < 100001):
        queue.append([2*n,c+1])


#1963
import sys,collections,math
# input = sys.stdin.readline
nums = ['0','1','2','3','4','5','6','7','8','9']
def isPrime(x):
    if(x == 2):
        return True
    if(x%2 == 0 or x == 1):
        return False
    for i in range(3,math.floor(math.sqrt(x)) + 1,2):
        if(x%i == 0):
            return False
    return True

for _ in range(int(input())):
    # a,b = input().rstrip().split()
    a,b = input().split()
    queue,visited = collections.deque([[a,0]]),[]    
    while(queue):
        a,c = queue.popleft()
        if(a == b):
            print(c)
            break
        if(a in visited):
            continue
        visited.append(a)
        
        s1,s2,s3,s4 = a
        nums.remove(s1)
        nums.remove('0')
        for num in nums:
            new = num+s2+s3+s4
            if(isPrime(int(new))):
                queue.append([new,c+1])
        nums.insert(0,'0')
        nums.insert(int(s1),s1)

        nums.remove(s2)
        for num in nums:
            new = s1+num+s3+s4
            if(isPrime(int(new))):
                queue.append([new,c+1])
        nums.insert(int(s2),s2)

        nums.remove(s3)
        for num in nums:
            new = s1+s2+num+s4
            if(isPrime(int(new))):
                queue.append([new,c+1])
        nums.insert(int(s3),s3)
        
        nums.remove(s4)
        for num in nums:
            new = s1+s2+s3+num
            if(isPrime(int(new))):
                queue.append([new,c+1])
        nums.insert(int(s4),s4)


#9019
#pypy에서 제출해야 풀림... 정수형으로
import sys,collections
input = sys.stdin.readline
for _ in range(int(input())):
    A,B = map(int,input().split())
    queue,visited = collections.deque([[A,'']]),[0]*10000
    visited[A] = 1
    while(queue):
        A,out = queue.popleft()
        if(A == B):
            print(out)
            break
        if(A>=5000):
            if 2*A-10000 == B:
                print(out + 'D')
                break
            if not visited[2*A-10000]:
                queue.append([2*A-10000, out+'D'])
                visited[2*A-10000] = 1
        else:
            if 2*A == B:
                print(out + 'D')
                break
            if not visited[2*A]:
                queue.append([2*A, out+'D'])
                visited[2*A] = 1
        if(A>0):
            if A-1 == B:
                print(out + 'S')
                break
            if not visited[A-1]:
                queue.append([A-1, out+'S'])
                visited[A-1] = 1
        else:
            if 9999 == B:
                print(out + 'S')
                break
            if not visited[9999]:
                queue.append([9999, out+'S'])
                visited[9999] = 1
        t = (A%1000)*10 + A//1000
        if t == B:
            print(out + 'L')
            break
        if not visited[t]:
            queue.append([t, out+'L'])
            visited[t] = 1
        t = (A%10)*1000 + A//10
        if t == B:
            print(out + 'R')
            break
        if not visited[t]:
            queue.append([t, out+'R'])
            visited[t] = 1


#1525
import collections
start = ''
for _ in range(3):
    start += input().replace(' ', '')
start = start.replace('0', '9')
dic, queue = {start:0}, collections.deque([start])
while(queue):
    que = queue.popleft()
    if(que == '123456789'):
        print(dic[que])
        break
    for index in range(9):
        if(que[index] == '9'):
            i = index
    #9가 왼쪽줄 아닐때
    if(i%3 != 0):
        tmp = que[:i-1]+que[i]+que[i-1]+que[i+1:]
        if tmp not in dic:
            dic[tmp] = dic[que] + 1
            queue.append(tmp)
    #9가 오른쪽줄 아닐때
    if(i%3 != 2):
        tmp = que[:i]+que[i+1]+que[i]+que[i+2:]
        if tmp not in dic:
            dic[tmp] = dic[que] + 1
            queue.append(tmp)
    #9가 윗줄 아닐때
    if(i>2):
        tmp = que[:i-3]+que[i]+que[i-2:i]+que[i-3]+que[i+1:]
        if tmp not in dic:
            dic[tmp] = dic[que] + 1
            queue.append(tmp)
    #9가 아랫줄 아닐때
    if(i<6):
        tmp = que[:i]+que[i+3]+que[i+1:i+3]+que[i]+que[i+4:]
        if tmp not in dic:
            dic[tmp] = dic[que] + 1
            queue.append(tmp)
if(que != '123456789'):
    print(-1)



#tq
def isAnswer(cube):
    for i in range(3):
        for j in range(3):
            if(cube[i][j] != 3*i+(j+1)):
                return False
    return True
def isVisited(c1,c2):
    for i in range(3):
        for j in range(3):
            if(c1[i][j] != c2[i][j]):
                return False
    return True
def i0(i,j,t,c):
    t = [line[:] for line in t]
    if(i!=0):
        if(t[i-1][j] != 3*(i-1)+(j+1)):
            t[i][j],t[i-1][j] = t[i-1][j],t[i][j]
            for c1 in visited:
                if isVisited(c1,t):
                    return 0
            visited.append(t)
            queue.append([i-1,j,t,c+1])
    if isAnswer(t):
        return 1
    else:
        return 0
def i2(i,j,t,c):
    t = [line[:] for line in t]
    if(i!=2):
        if(t[i+1][j] != 3*(i+1)+(j+1)):
            t[i][j],t[i+1][j] = t[i+1][j],t[i][j]
            for c1 in visited:
                if isVisited(c1,t):
                    return 0
            visited.append(t)
            queue.append([i+1,j,t,c+1])
    if isAnswer(t):
        return 1
    else:
        return 0
def j0(i,j,t,c):
    t = [line[:] for line in t]
    if(j!=0):
        if(t[i][j-1] != 3*(i)+(j)):
            t[i][j],t[i][j-1] = t[i][j-1],t[i][j]
            for c1 in visited:
                if isVisited(c1,t):
                    return 0
            visited.append(t)
            queue.append([i,j-1,t,c+1])
    if isAnswer(t):
        return 1
    else:
        return 0
def j2(i,j,t,c):
    t = [line[:] for line in t]
    if(j!=2):
        if(t[i][j+1] != 3*(i)+(j+2)):
            t[i][j],t[i][j+1] = t[i][j+1],t[i][j]
            for c1 in visited:
                if isVisited(c1,t):
                    return 0
            visited.append(t)
            queue.append([i,j+1,t,c+1])
    if isAnswer(t):
        return 1
    else:
        return 0
    
import collections
#cube 완성
cube = []
for _ in range(3):
    cube.append(list(map(int,input().split())))
queue = collections.deque([])
#start
for i in range(3):
    for j in range(3):
        if(cube[i][j] == 0):
            cube[i][j] = 9
            queue.append([i,j,cube,0])
visited = [[line[:] for line in cube]]
while(queue):
    i,j,t,c = queue.popleft()
    if(i0(i,j,t,c)): 
        print(c+1)
        break
    if(i2(i,j,t,c)):
        print(c+1)
        break
    if(j0(i,j,t,c)):
        print(c+1)
        break
    if(j2(i,j,t,c)):
        print(c+1)
        break
    

#2251
import collections
A,B,C = map(int,input().split())
queue,visited = collections.deque([[0,0,C]]),[]
while(queue):
    a,b,c = queue.popleft()
    if([a,b,c] in visited):
        continue
    visited.append([a,b,c])
    #A에서 물을 주는경우
    if(a != 0 and b<B):
        if(a+b <= B):
            queue.append([0,a+b,c])
        else:
            queue.append([a+b-B,B,c])
    if(a != 0 and c<C):
        if(a+c <= C):
            queue.append([0,b,a+c])
        else:
            queue.append([a+c-C,b,C])
    #B에서 물을 주는경우
    if(b != 0 and a<A):
        if(b+a <= A):
            queue.append([a+b,0,c])
        else:
            queue.append([A,a+b-A,c])
    if(b != 0 and c<C):
        if(b+c <= C):
            queue.append([a,0,b+c])
        else:
            queue.append([a,b+c-C,C])
    #C에서 물을 주는경우
    if(c != 0 and a<A):
        if(c+a <= A):
            queue.append([a+c,b,0])
        else:
            queue.append([A,b,a+c-A])
    if(c != 0 and b<B):
        if(b+c <= B):
            queue.append([a,b+c,0])
        else:
            queue.append([a,B,b+c-B])
output = [w for w in visited if w[0]==0]
output.sort(key = lambda x : x[2])
print(' '.join([str(a[2]) for a in output]))


#2186 pypy로 제출해야함 bfs는 메모리초과뜬다. dfs에 메모이제이션을 사용해야한다고함. 머리터진다...
#최종
import sys
N,M,K = map(int,sys.stdin.readline().split())
alpha = []
for _ in range(N):
    alpha.append(sys.stdin.readline().rstrip())
answer = sys.stdin.readline()
length = len(answer) - 1
visited = [[[-1]*length for _ in range(M)] for _ in range(N)]
def dfs(i,j,l):
    if(visited[i][j][l] >= 0):
        return visited[i][j][l]
    if(l == length - 1):
        return 1    
    visited[i][j][l] = 0
    for x in range(1,K+1):
        if((i-x)>=0 and alpha[i-x][j] == answer[l+1]):
            visited[i][j][l] += dfs(i-x,j,l+1)
        if((i+x)<N and alpha[i+x][j] == answer[l+1]):
            visited[i][j][l] += dfs(i+x,j,l+1)
    for y in range(1,K+1):
        if((j-y)>=0 and alpha[i][j-y] == answer[l+1]):
            visited[i][j][l] += dfs(i,j-y,l+1)
        if((j+y)<M and alpha[i][j+y] == answer[l+1]):
            visited[i][j][l] += dfs(i,j+y,l+1)    
    return visited[i][j][l]
output = 0
for i in range(N):
    for j in range(M):
        if alpha[i][j] == answer[0]:
            output += dfs(i,j,0)
print(output)

#dfs
import sys,collections
input = sys.stdin.readline

N,M,K = map(int,input().split())
alpha = []
for _ in range(N):
    alpha.append(input().rstrip())
answer = input().rstrip()
length = len(answer)

visited = [[[-1]*length for _ in range(M)] for _ in range(N)]

def dfs(i,j,l):
    if(visited[i][j][l] >= 0):
        return visited[i][j][l]
    if(l == length - 1):
        return 1
    
    #-1로 초기화했었으므로
    visited[i][j][l] = 0
    for x in range(1,K+1):
        if((i-x)>=0 and alpha[i-x][j] == answer[l+1]):
            visited[i][j][l] += dfs(i-x,j,l+1)
        if((i+x)<N and alpha[i+x][j] == answer[l+1]):
            visited[i][j][l] += dfs(i+x,j,l+1)
    for y in range(1,K+1):
        if((j-y)>=0 and alpha[i][j-y] == answer[l+1]):
            visited[i][j][l] += dfs(i,j-y,l+1)
        if((j+y)<M and alpha[i][j+y] == answer[l+1]):
            visited[i][j][l] += dfs(i,j+y,l+1)
    
    return visited[i][j][l]

output = 0
for i in range(N):
    for j in range(M):
        if alpha[i][j] == answer[0]:
            output += dfs(i,j,0)

print(output)


#3108 
import sys, collections
input = sys.stdin.readline

N = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue,starts = collections.deque([]),[]
graph = [[0]*2001 for _ in range(2001)]

c = [[0]*2001 for _ in range(2001)]

for _ in range(N):
    x1,y1,x2,y2 = map(int,input().split())
    x1,y1,x2,y2 = 2*x1+1000,2*y1+1000,2*x2+1000,2*y2+1000
    starts.append([x1,y1])
    for i in range(x1,x2+1):
        if i==x1 or i==x2:
            for j in range(y1, y2+1):
                graph[i][j] = 1
        else:
            graph[i][y1] = 1
            graph[i][y2] = 1
    # for x in range(x1,x2+1):
    #     graph[x][y1], graph[x][y2] = 1,1
    # for y in range(y1+1,y2):
    #     graph[x1][y], graph[x2][y] = 1,1

if graph[1000][1000] == 1:
    output = -1
else:
    output = 0

for a,b in starts:
    if(c[a][b] == 0):
        queue.append([a,b])
        c[a][b] = 1
        while(queue):
            x,y = queue.popleft()
            for t in range(4):
                i,j = x+dx[t],y+dy[t]
                if(0<=i<2001) and (0<=j<2001) and (graph[i][j] == 1) and (c[i][j] == 0):
                    c[i][j] = 1
                    queue.append([i,j])
        output += 1        
print(output)

#이게 메모리 적게쓰고 빠른거같은데 왜 더느리냐ㅠㅠㅠㅠㅠ
for a,b in starts:
    if(graph[a][b] == 0):
        output -= 1
        continue
    queue.append([a,b])
    while(queue):
        x,y = queue.popleft()
        graph[x][y] = 0
        for t in range(4):
            i,j = x+dx[t],y+dy[t]
            if(0<=i<2001) and (0<=j<2001) and (graph[i][j] == 1):
                queue.append([i,j])
                
print(output)

#나의 dfs풀이 bfs는 오류나고 이건 겁나 빠르네 왤까
import sys, collections
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue,starts = collections.deque([]),[]
graph = [[0]*2001 for _ in range(2001)]
for _ in range(N):
    x1,y1,x2,y2 = map(int,input().split())
    x1,y1,x2,y2 = 2*x1+1000,2*y1+1000,2*x2+1000,2*y2+1000
    starts.append([x1,y1])
    for i in range(x1,x2+1):
        if i==x1 or i==x2:
            for j in range(y1, y2+1):
                graph[i][j] = 1
        else:
            graph[i][y1] = 1
            graph[i][y2] = 1            
if graph[1000][1000] == 1:
    output = N-1
else:
    output = N
def dfs(x,y):
    graph[x][y] = 0
    for t in range(4):
        i,j = x+dx[t],y+dy[t]
        if(0<=i<2001) and (0<=j<2001) and (graph[i][j] == 1):
            dfs(i,j)
for a,b in starts:
    if(graph[a][b] == 0):
        output -= 1
        continue
    dfs(a,b)    
print(output)




#5014 3분컷
import collections
F,S,G,U,D = map(int,input().split())
queue,visited = collections.deque([[S,0]]), [0]*(F+1)
while(queue):
    s,o = queue.popleft()
    if(s == G):
        print(o)
        break
    if(visited[s]):
        continue
    visited[s] = 1
    if(s-D>0):
        queue.append([s-D,o+1])
    if(s+U<=F):
        queue.append([s+U,o+1])
if(s != G):
    print('use the stairs')


#1759
import itertools
L,C = map(int,input().split())
alpha = sorted(input().rstrip().split())
#x:모음 y:자음
x,y = [],[]
for i in range(C):
    if alpha[i] in ['a','e','i','o','u']:
        x.append(i)
    else:
        y.append(i)
#combinations를 이용하면 증가하는 순서대로 나온다.
for element in itertools.combinations(list(range(C)), L):
    #n:모음 m:자음
    n,m = 0,0
    #모음이 한개, 자음이 두개이상 있어야한다.
    for index in element:
        if(index in x):
            n+=1
        else:
            m+=1
    if(n==0 or m<2):
        continue
    #만족하면 출력    
    print(''.join([alpha[i] for i in element]))


#2580



#사각형을 탐색해보니 한군데만 비어있으면 숫자채워주기. 이걸... 초딩이푼다고...? pypy제출. python은 82%.
graph = [input().rstrip().split() for _ in range(9)]
queue = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == '0':
            queue.append([i,j])
            
def check(a,b):
    nums = [str(i) for i in range(1,10)]
    #사각형안
    x,y = a-a%3, b-b%3
    for i in range(3):
        for j in range(3):
            if graph[x+i][y+j] in nums:
                nums.remove(graph[x+i][y+j])
    #가로
    for j in range(9):
        if graph[a][j] in nums:
            nums.remove(graph[a][j])
    #세로
    for i in range(9):
        if graph[i][b] in nums:
            nums.remove(graph[i][b])
    if(nums):        
        return nums
    else:
        return 0

def dfs(n):
    if n==len(queue):
        for line in graph:
            print(' '.join(line))
        exit()
    x,y = queue[n]
    nums = check(x,y)
    if not nums:
        return
    for num in nums:
        graph[x][y] = num
        dfs(n+1)
        graph[x][y] = '0'

dfs(0)


graph = [['0', '3', '5', '4', '6', '9', '2', '7', '8'],
 ['7', '8', '2', '1', '0', '5', '6', '0', '9'],
 ['0', '6', '0', '2', '7', '8', '1', '3', '5'],
 ['3', '2', '1', '0', '4', '6', '8', '9', '7'],
 ['8', '0', '4', '9', '1', '3', '5', '0', '6'],
 ['5', '9', '6', '8', '2', '0', '4', '1', '3'],
 ['9', '1', '7', '6', '5', '2', '0', '8', '0'],
 ['6', '0', '3', '7', '0', '1', '9', '5', '2'],
 ['2', '5', '8', '3', '9', '4', '7', '6', '0']]

sdoku = [[0, 3, 5, 4, 6, 9, 2, 7, 8],
 [7, 8, 2, 1, 0, 5, 6, 0, 9],
 [0, 6, 0, 2, 7, 8, 1, 3, 5],
 [3, 2, 1, 0, 4, 6, 8, 9, 7],
 [8, 0, 4, 9, 1, 3, 5, 0, 6],
 [5, 9, 6, 8, 2, 0, 4, 1, 3],
 [9, 1, 7, 6, 5, 2, 0, 8, 0],
 [6, 0, 3, 7, 0, 1, 9, 5, 2],
 [2, 5, 8, 3, 9, 4, 7, 6, 0]]

# 제출용
# import sys
# input = sys.stdin.readline
# graph = [input().split() for _ in range(9)]
# queue = []
# for i in range(9):
#     for j in range(9):
#         if graph[i][j] == '0':
#             queue.append([i,j])
# def check(a,b):
#     nums = [str(i) for i in range(1,10)]
#     x,y = a-a%3, b-b%3
#     for i in range(3):
#         for j in range(3):
#             if graph[x+i][y+j] in nums:
#                 nums.remove(graph[x+i][y+j])
#     for j in range(9):
#         if graph[a][j] in nums:
#             nums.remove(graph[a][j])
#     for i in range(9):
#         if graph[i][b] in nums:
#             nums.remove(graph[i][b])
#     if(nums):        
#         return nums
#     else:
#         return 0
# def dfs(n):
#     if n==len(queue):
#         for line in graph:
#             print(' '.join(line))
#         exit()
#     x,y = queue[n]
#     nums = check(x,y)
#     if not nums:
#         return
#     for num in nums:
#         graph[x][y] = num
#         dfs(n+1)
#         graph[x][y] = '0'
# dfs(0)


#1987
#set으로 변경, dx,dy 설정하는게 속도차이가 꽤 나는듯.
R,C = map(int,input().split())
graph,output = [],0
for _ in range(R):
    graph.append(input())
visited = set(graph[0][0])
dx,dy = [1,-1,0,0], [0,0,1,-1]
def dfs(i,j,c):
    global output
    output = max(output,c)
    if output == 26:
        return
    for m in range(4):
        x,y= i+dx[m],j+dy[m]
        if (0<=x<R) and (0<=y<C) and (graph[x][y] not in visited):
            visited.add(graph[x][y])
            dfs(x,y,c+1)
            visited.remove(graph[x][y])
                
dfs(0,0,1)
print(output)

#
R,C = map(int,input().split())
graph,output = [],0
for _ in range(R):
    graph.append(input().rstrip())
visited = [graph[0][0]]
dx,dy = [1,-1,0,0], [0,0,1,-1]
def dfs(i,j,c):
    global output
    output = max(output,c)
    if output == 26:
        return
    for m in range(4):
        x,y= i+dx[m],j+dy[m]
        if (0<=x<R) and (0<=y<C) and (graph[x][y] not in visited):
            visited.append(graph[x][y])
            dfs(x,y,c+1)
            visited.pop()
dfs(0,0,1)
print(output)


#6603
import itertools
stop = 1
while(stop):
    tmp = input().rstrip().split()
    k,s = int(tmp[0]), tmp[1:]
    c = itertools.combinations(list(range(k)),6)
    for order in c:
        print(' '.join([s[i] for i in order]))
    print('')
    stop = k


#1182
#모든 부분집합 탐색
import itertools
n,s = map(int,input().split())
nums = list(map(int,input().split()))
output = 0
for d in range(1,n+1):
    for order in itertools.combinations(list(range(n)),d):
        tmp = 0
        for o in order:
            tmp += nums[o]
        if tmp == s :
            output += 1
print(output)


#2003
import collections
N,M = map(int,input().split())
nums = list(map(int,input().split()))
output = 0
i = 1
summ = collections.deque([0])
while(i <= N):
    if sum([nums[i] for i in summ]) < M :
        summ.append(i)
        i += 1
    elif sum([nums[i] for i in summ]) == M :
        output += 1
        summ.popleft()
    else:
        summ.popleft()
print(output)
        

#1806
#윈도우사이즈로 하자. 초기 윈도우사이즈는 S값과 최댓값사이의 관계로.
#summ을 만드는데 시간이 많이드는것같다. 처음부터 현재까지의 합들로 구성하고 뺄샘으로 비교하자.
N,S = map(int,input().split())
nums = list(map(int,input().split()))
size = S//max(nums)
summ = [0]*(N+1)
for i in range(N):
    summ[i+1] = summ[i] + nums[i]
def f():
    s,e,o = 0,size,N+1
    while(s <= N-size):
        if summ[e] - summ[s] >= S:
            o = min(o, e-s)
            s+=1
        else:
            if(e < N):
                e += 1
            else:
                break
    if o != N+1 :
        print(o)
    else:
        print(0)
f()


#1644
#에라토스테네스의 체
import math
N = int(input())
if(N==1):
    print(0)
    exit()
table = [0,0] + [1]*(N-1)
primes = []
start = 2
while(start <= math.floor(N**0.5)):
    primes.append(start)
    for i in range(start,N+1,start):
        table[i] = 0
    for i in range(start, N+1):
        if table[i] == 1:
            start = i
            break
for i in range(start, N+1):
    if table[i] == 1:
        primes.append(i)

length = len(primes)
summ = [0]*(length+1)
for i in range(length):
    summ[i+1] = summ[i] + primes[i]

output = 0
for i in range(length):
    for j in range(i+1,length+1):
        if(summ[j] - summ[i] == N):
            output += 1
        elif(summ[j] - summ[i] > N):
            break

print(output)


#1261 BFS로 벽없으면 왼쪽에 벽있으면 오른쪽에 추가
import sys,collections
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[int(s) for s in input().rstrip()] for _ in range(M)]
visited = [[1]*N for _ in range(M)]
dx,dy = [-1,1,0,0], [0,0,-1,1]
queue = collections.deque([[0,0,0]])
output = 0
while(queue):
    x,y,c = queue.popleft()
    if x == M-1 and y == N-1:
        print(c)
        break
    if(visited[x][y]):
        visited[x][y] = 0
        for t in range(4):
            i,j = x+dx[t], y+dy[t]
            if(0<=i<M) and (0<=j<N):
                if(graph[i][j] == 1):
                    queue.append([i,j,c+1])
                else:
                    queue.appendleft([i,j,c])

#dfs 시간초과
count = N*M
def dfs(i,j,c):
    global count
    if c == count:
        return
    if i==M-1 and j==N-1 :
        count = c
        return
    if(visited[i][j]):
        visited[i][j] = 0
        for t in range(4):
            x,y = i+dx[t], j+dy[t]
            if (0<=x<M) and (0<=y<N):
                if graph[i][j] == 1:
                    dfs(x,y,c+1)
                else:
                    dfs(x,y,c)
        visited[i][j] = 1
dfs(0,0,0)
print(count)


#1208
from itertools import combinations
N,S = map(int,input().split())
nums = list(map(int,input().split()))
nums1 = nums[:N//2]
nums2 = nums[N//2:]
summ1, summ2 = [], []

for i in range(len(nums1)+1):
    c1 = combinations(nums1,i)
    for sub1 in c1:
        summ1.append(sum(sub1))
for i in range(len(nums2)+1):
    c2 = combinations(nums2,i)
    for sub2 in c2:
        summ2.append(sum(sub2))

summ1,summ2 = sorted(summ1), sorted(summ2)

l,r = 0, len(summ2)-1
output = 0
#왼쪽 오른쪽에서 아무것도 안뽑는경우 빼주자.
if S == 0:
    output -= 1
    
while l< len(summ1) and r>=0 :
    summ = summ1[l] + summ2[r]    
    if summ == S:
        c1,c2 = 1,1
        ll,rr = l,r
        
        #같은값인것들 체크해서 더해주기
        l,r = l+1, r-1
        while l < len(summ1) and summ1[l] == summ1[ll]:
            c1 += 1
            l += 1
        while r >= 0 and summ2[r] == summ2[rr]:
            c2 += 1
            r -= 1
        
        output += (c1*c2)
    
    elif summ < S:
        l += 1
    else:
        r -= 1

print(output)




#7453
#그냥 dict로 해보자 ㅡㅡ; 되네. defaultdict 다신안써 ㅅㅄ
import sys
input = sys.stdin.readline

n = int(input())
A,B,C,D = {},{},{},{}
for _ in range(n):
    a,b,c,d = map(int,input().split())
    if a not in A:
        A[a] = 1
    else :
        A[a] += 1
    if b not in B:
        B[b] = 1
    else :
        B[b] += 1
    if c not in C:
        C[c] = 1
    else :
        C[c] += 1
    if d not in D:
        D[d] = 1
    else :
        D[d] += 1

summ1 = {}

for k1 in A:
    for k2 in B:
        if k1+k2 not in summ1:
            summ1[k1+k2] = A[k1]*B[k2]
        else :
            summ1[k1+k2] += A[k1]*B[k2]

output = 0
for k1 in C:
    for k2 in D:
        if -k1-k2 in summ1:
            output += summ1[-k1-k2]*(C[k1]*D[k2])

print(output)


#이게 왜초과냐고 ㅡㅡ 뭐야 풀이코드들도 시간초과뜨네 pypy에서 해야하는구나.
import sys,collections
input = sys.stdin.readline

n = int(input())
A,B,C,D = collections.defaultdict(int),collections.defaultdict(int),collections.defaultdict(int),collections.defaultdict(int)
for _ in range(n):
    a,b,c,d = map(int,input().split())
    A[a] += 1
    B[b] += 1
    C[c] += 1
    D[d] += 1

summ1 = collections.defaultdict(int)

for k1 in A:
    for k2 in B:
        summ1[k1+k2] += A[k1]*B[k2]

output = 0
for k1 in C:
    for k2 in D:
        output += summ1[-k1-k2]*(C[k1]*D[k2])

print(output)



#2632
import sys
input = sys.stdin.readline

s = int(input())
m,n = map(int,input().split())
p1,p2 = [],[]
for _ in range(m):
    p1.append(int(input()))
for _ in range(n):
    p2.append(int(input()))
summ1, summ2 = {0:1, sum(p1):1}, sum(p2)
p1,p2 = p1+p1, p2+p2


for i in range(m):
    for win in range(1,m):
        tmp = sum(p1[i:i+win])
        summ1[tmp] = summ1.get(tmp,0) + 1
    
output = 0

for i in range(n):
    for win in range(1,n):
        tmp = sum(p2[i:i+win])
        output += summ1.get(s-tmp,0)

#왼쪽피자만 사용했을때 추가
output += summ1.get(s,0)
#한바퀴 다돈값 있으면 추가
output += summ1.get(s-summ2,0)
print(output)



#2143 마지막!!! 꺄륵!!
T = int(input())
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

summ1, summ2 = [0]*(n+1),[0]*(m+1)
for i in range(n):
    summ1[i+1] = summ1[i] + A[i]
for i in range(m):
    summ2[i+1] = summ2[i] + B[i]

summA = {}
for i in range(n):
    for j in range(i+1,n+1):
        tmp = summ1[j] - summ1[i]
        summA[tmp] = summA.get(tmp,0) + 1
        
output = 0
for i in range(m):
    for j in range(i+1, m+1):
        tmp = summ2[j] - summ2[i]
        if T-tmp in summA:
            output += summA[T-tmp]

print(output)














