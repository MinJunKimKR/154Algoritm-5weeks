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











