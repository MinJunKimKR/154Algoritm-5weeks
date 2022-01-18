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
n = int(input())
import math
output = 0
for i in range(int((n+2)//2)):
    output += (math.factorial(n-i) // math.factorial(n-2*i) // math.factorial(i))
    if(output>10007):
         output %= 10007
print(output)

#11727
n = int(input())
import math
output = 0
for i in range(int((n+2)//2)):
    output += (math.factorial(n-i) // math.factorial(n-2*i) // math.factorial(i))*(2**i)
    if(output>10007):
         output %= 10007
print(output)

#9095
T = int(input())
while(T):
    n = int(input())
    if n<4 : 
        start = [1,2,4]
        print(start[n-1])
    else:
        a,b,c = 1,2,4
        for i in range(n-3):
            a,b,c = b,c,a+b+c
        print(c)
    T -= 1

#10844
N = int(input())
dp = [[0,1,1,1,1,1,1,1,1,1]]
for i in range(N-1):
    new = [dp[i][1]] + [0]*8 + [dp[i][8]]
    for j in range(1,9):
        new[j] = dp[i][j-1] + dp[i][j+1]
    dp.append(new)
print(sum(dp[-1])%1000000000)

# from collections import deque
# nums = deque(['1','2','3','4','5','6','7','8','9'])
# N -= 1
# while(N):
#     for _ in range(len(nums)):
#         num = nums.popleft()
#         if(num[-1]=='0'):
#             nums.append(num+'1')
#         elif(num[-1]=='9'):
#             nums.append(num+'8')
#         else:
#             nums.append(num+str(int(num[-1])-1))
#             nums.append(num+str(int(num[-1])+1))
#     N -=1
# print(len(nums)%(10**9))

#11057
N = int(input())
dp = [[1,1,1,1,1,1,1,1,1,1]]
for i in range(N-1):
    next_line = dp[-1]
    for j in range(1,10):
        next_line[j] += next_line[j-1]
    dp.append(next_line)
print(sum(dp[-1])%10007)

#2193
"""
0으로 끝나는개수 1로끝나는개수
0   1       1
1   0       10
1   1       100 101
2   1       1000 1001 1010
"""
N = int(input())
n1, n2 = 0, 1
while(N-1):
    n1, n2 = n1+n2, n1
    N -= 1
print(n1+n2)

#9465
def DP():
    N = int(input())
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    if(N==1):
        print(max(l1[0],l2[0]))
    else:
        #
        s1 = [l1[0], l2[0]+l1[1]]
        s2 = [l2[0], l1[0]+l2[1]]
        for line in range(2,N):
            s1.append(max(s2[line-2]+l1[line],s2[line-1]+l1[line]))
            s2.append(max(s1[line-2]+l2[line],s1[line-1]+l2[line]))
        print(max(s1[-1],s2[-1]))
T = int(input())
while(T):
    DP()
    T -= 1
        
#2156
n = int(input())
wines = []
for _ in range(n):
    wines.append(int(input()))
if(n==1):
    print(wines[0])
else:
    #s0 : 앞으로 o가 불가능한그룹 / s1 : xo / s11 : ox / s2 : o2개가능
    #oo xo ox xx
    s0,s1,s11,s2 = wines[0]+wines[1], wines[1], wines[0], 0
    for i in range(2,n):
        s0,s1,s11,s2 = s1+wines[i], max(s11+wines[i],s2+wines[i]), max(s0,s1), s11
    print(max(s0,s1,s11,s2))

#11053
N = int(input())
A = list(map(int,input().split()))
table = []
output = 1
for num in A:
    maximum = 1
    for record in table:
        if(record[0] < num):
            maximum = max(maximum,record[1]+1)
    table.append([num, maximum])
    output = max(maximum,output)
print(output)

#11055
N = int(input())
sequence = list(map(int,input().split()))
dp = []
for num in sequence:
    summ = num
    for n,s in dp:
        if(num > n):
            summ = max(summ, s+num)
    dp.append([num,summ])
output = dp[0][1]
for num, summ in dp:
    output = max(output,summ)
print(output)
            
#11722
N = int(input())
sequence = list(map(int,input().split()))
dp = []
for num in sequence:
    length = 1
    for n,l in dp:
        if(num < n):
            length = max(length, l+1)
    dp.append([num,length])
output = dp[0][1]
for num, length in dp:
    output = max(output,length)
print(output)

#11054
N = int(input())
sequence1 = list(map(int,input().split()))
sequence2 = sequence1[::-1]
dp1,dp2=[],[]
for num1,num2 in zip(sequence1,sequence2):
    length1,length2 = 1,1
    for [n1,l1],[n2,l2] in zip(dp1,dp2):
        if(num1>n1):
            length1 = max(length1,l1+1)
        if(num2>n2):
            length2 = max(length2,l2+1)
    dp1.append([num1,length1])
    dp2.append([num2,length2])
output = dp1[0][1]+dp2[N-1][1]
for i in range(N):
    output = max(output, dp1[i][1]+dp2[N-1-i][1])
print(output - 1)

#1912
N = int(input())
sequence = list(map(int,input().split()))
dp = []
for i,num in enumerate(sequence):
    if(i==0):
        maximum = num
        dp.append([num,num])
    else:
        maximum = max(num,dp[i-1][1]+num)
        dp.append([num,maximum])
output = dp[0][1]
for n,s in dp:
    output = max(output, s)
print(output)

#2579
N = int(input())
sequence = []
for _ in range(N):
    sequence.append(int(input()))
if(N==1):
    print(sequence[0])
elif(N==2):
    print(sequence[0]+sequence[1])
elif(N==3):
    print(max(sequence[0]+sequence[2],sequence[2]+sequence[1]))
else:
    sequence = sequence[::-1]
    #xo ox
    s11,s22 = sequence[0]+sequence[2], sequence[0]+sequence[1]
    #oo ox xo 
    s1,s2,s3 = s11+sequence[3],s11,s22+sequence[3]
    for i in range(4,N):
        s1,s2,s3 = sequence[i]+s3, max(s3,s1), sequence[i]+s2
    print(max(s1,s2,s3))

#1699
n = int(input())
dp = [0 for i in range(n + 1)]
square = [i * i for i in range(1, 317)]
for i in range(1, n + 1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i - j])
    dp[i] = min(s) + 1
print(dp[n])

#1699 공부하고 수정해서 좀더빨라
n = int(input())
import math
dp = [0 for i in range(n + 1)]
square = [i * i for i in range(1, math.ceil(math.sqrt(n))+1)]
for i in range(1,n+1):
    #dp[i] = dp[i - square에서 뽑은 sq]+1
    dp[i] = dp[i-1] + 1
    for sq in square[1:math.floor(math.sqrt(i))]:
        if dp[i-sq] + 1 < dp[i]:
            dp[i] = dp[i-sq] + 1
print(dp[n])
        
#2133
N = int(input())
if(N%2 == 1): 
    print(0)
else:
    N //= 2
    sequence = [3,11]
    if(N<3):
        print(sequence[N-1])
    else:
        for i in range(2,N):
            #sequence[i-1]*3 : first, +2 : last
            pos = sequence[i-1]*3 + 2
            for j in range(i-2,-1,-1):
                pos += sequence[j] * 2
            sequence.append(pos)
        print(sequence[-1])
        

#9461
#first 0 of sequence : padding
T = int(input())
N_list = []
while(T):    
    N_list.append(int(input()))
    T -= 1
max_num = max(N_list)
sequence = [0,1,1,1,2,2]
if(max_num<6) :
    pass
else:
    for i in range(6,max_num+1):
        sequence.append(sequence[i-1]+sequence[i-5])
for num in N_list :
    print(sequence[num])

#2225
#     N=1,2,3...
# k=1[  1,1,1,1...]
# k=2[  2,3,4,5...]
# k=3[  3,6,10,15...]
# k=4[  4,10,20,25...]
N,K = map(int,input().split())
dp = [[1]*N]
for i in range(1,K):
    dp.append([i+1] + [0]*(N-1))
if(N>1 and K>1):
    for m in range(1,K):
        for n in range(1,N):
            dp[m][n] = dp[m-1][n] + dp[m][n-1]
print(dp[K-1][N-1]%1000000000)

#2011
#1000000으로 나눈 나머지를 출력한다.
#암호를 해석할 수 없는 경우에는 0을 출력
"""2개짜리 윈도우로 검사하는데 
  뒤가0이면 해독가능한지 판단
      가능하면 전전숫자만 가져오기
  앞이0이면 전숫자만가져오기
  두자리가 11~26이면 전숫자와 전전숫자더하기
  두자리가 27~이면 전숫자만 가져오기
"""
password = input()
length = len(password)
if(password[0] == '0'):
    print(0)
elif(length == 1):
    print(1)
elif(length == 2):
    if(int(password) < 27):
        print(2)
    elif(password[1] == '0'):
        print(0)
    else: print(1)
else:
    #first 1 is padding
    dp = [1,1]
    for i in range(length-1):
        num = password[i:i+2]
        #뒤가0이면 해독가능한지 판단 가능하면 전전숫자 추가 아니면 리턴
        if(num[1] == '0'):
            if(num[0] not in ['1','2']):
                print(0)
                break
            else:
                dp.append(dp[i])
        else:
            #앞이0이면 전숫자만가져오기
            if(num[0] == '0'):
                dp.append(dp[i+1])
            #두자리가 11~26이면 전숫자와 전전숫자더하기
            elif(int(num) < 27):
                dp.append(dp[i]+dp[i+1])
            #두자리가 27~이면 전숫자만 가져오기
            else:
                dp.append(dp[i+1])
    if(len(dp) == length+1): print(dp[-1]%1000000)
    print(dp)
            
#11052
N = int(input())
prices = list(map(int,input().split()))
dp,length = [prices[0]], len(prices)
for i in range(1,length):
    maximum = prices[i]
    for j in range(0,(i+1)//2):
        maximum = max(maximum, dp[j] + dp[i-1-j])    
    dp.append(maximum)
print(dp[-1])





















