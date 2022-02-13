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
    





















            






