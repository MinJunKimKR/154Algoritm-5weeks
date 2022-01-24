#map(int,os.read(0, 100000000).decode('utf-8').split('\n'))


#2557
print("Hello World!")

#1000
a, b = map(int, input().split())
print(a+b)

#2558
a = int(input())
b = int(input())
print(a+b)

#10950
T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    print(a+b)
    
#   10951
try:
    while(1):
        a,b = map(int,input().split())
        print(a+b)
except:
    exit()

#10952
try:
    while(1):
        a,b = map(int,input().split())
        print(a+b) if a != 0 else exit()
except:
    exit()
    
#10953
T = int(input())
for i in range(T):
    a,b = map(int,input().split(','))
    print(a+b)

#11021
T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    print(f'Case #{i+1}: {a+b}')

#11022
T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')

#11718, 11719
try:
    while(1):
        string = input()
        print(string)
except:
    exit()

#11720
T = int(input())
nums = input()
output = 0
for i in range(T):
    output += int(nums[i])
print(output)

#11721
strings = input()
string = ''
for alpha in strings:
    if len(string) == 10 :
        print(string)
        string = alpha
    else: 
        string += alpha
if string : print(string)

#2741
N = int(input())
for i in range(1,N+1):
    print(i)

#2742
N = int(input())
for i in range(N,0,-1):
    print(i)

#2739
N = int(input())
for i in range(1,10):
    print(f'{N} * {i} = {N*i}')

#1924
mon, day = map(int, input().split())
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
days_of_month = [31,28,31,30,31,30,31,31,30,31,30,31]
out = 0
for i in range(mon-1):
    out += days_of_month[i]
out += day
out = out % 7
print(days[out])

#8393
n = int(input())
print(int(n*(n+1)/2))

#10818
_=input()
nums = list(map(int, input().split()))
print(f'{min(nums)} {max(nums)}')

#2438 별찍기 시리즈
N = int(input())
for i in range(1,N+1):
    print('*'*i)
#2439
N = int(input())
for i in range(1,N+1):
    print(' '*(N-i) + '*'*i)
#2440
N = int(input())
for i in range(N,0,-1):
    print('*'*i)
#2441
N = int(input())
for i in range(N,0,-1):
    print(' '*(N-i) + '*'*i)
#2442
N = int(input())
for i in range(1,N+1):
    print(' '*(N-i) + '*'*(2*i-1))
#2445
N = int(input())
for i in range(1,N+1):
    print('*'*i + ' '*(2*(N - i)) + '*'*i)
for i in range(N-1,0,-1):
    print('*'*i + ' '*(2*(N - i)) + '*'*i)
#2522
N = int(input())
for i in range(1,N+1):
    print(' '*(N - i) + '*'*i)
for i in range(N-1,0,-1):
    print(' '*(N - i) + '*'*i)
#2446
N = int(input())
for i in range(N,0,-1):
    print(' '*(N-i) + '*'*(2*i - 1))
for i in range(2,N+1):
    print(' '*(N-i) + '*'*(2*i - 1))
#10991
N = int(input())
for i in range(1,N+1):
    print(' '*(N-i) + '* '*(i-1) + '*')
#10992
N = int(input())
if(N==1):
    print("*")
elif(N==2):
    print(" *")
    print("***")
else:
    print(' '*(N-1) + "*")
    for i in range(2,N):
        print(' '*(N-i)+ '*' + ' '*(2*i-3) + '*')
    print('*'*(2*N - 1))



# DP start
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



#Sorting

#2751
import sys
N = int(sys.stdin.readline())
sequence = []
for _ in range(N):
    sequence.append(int(sys.stdin.readline()))
sequence.sort()
for num in sequence:
    print(num)

#solution
print(''.join(sorted(sys.stdin.readlines()[1:], key=int)))


#11650
import sys
N = int(sys.stdin.readline())
sequence = []
for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    sequence.append([x,y])
sequence.sort(key=lambda x: (x[0],x[1]))
for x,y in sequence:
    print(f'{x} {y}')

#11651
import sys
N = int(sys.stdin.readline())
sequence = []
for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    sequence.append([x,y])
sequence.sort(key=lambda x: (x[1],x[0]))
for x,y in sequence:
    print(f'{x} {y}')


#10814
import sys
N = int(sys.stdin.readline())
sequence = []
for i in range(N):
    age,name = sys.stdin.readline().split()
    sequence.append((int(age),name,i))
sequence.sort(key=lambda x: (x[0],x[2]))
for age,name,i in sequence:
    print(age, name)


#10825
import sys
N = int(sys.stdin.readline())
sequence = []
for i in range(N):
    name,k,e,m = sys.stdin.readline().split()
    sequence.append([name,int(k),int(e),int(m)])
sequence.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for person in sequence:
    print(person[0])


#10989
import sys
N = int(sys.stdin.readline())
sequence = [0]*10000
for i in range(N):
    num = int(sys.stdin.readline())
    sequence[num-1] += 1

for i,num in enumerate(sequence):
    for j in range(num):
        print(i+1)


#11652
import sys
from collections import defaultdict
N = int(sys.stdin.readline())
dic = defaultdict(int)
for i in range(N):
    dic[int(sys.stdin.readline())] += 1

sequence = sorted(list(dic.items()),key=lambda x: (-x[1],x[0]))
print(sequence[0][0])


#11004
import sys
N,K = map(int,sys.stdin.readline().split())
seq = list(map(int,sys.stdin.readline().split()))
seq.sort()
print(seq[K-1])



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



#String
import sys,collections
a = sys.stdin.readline()

#10808
string = input()
num_of_alpha,dic,output = [0]*26, {}, ''
for i,alpha in enumerate('abcdefghijklmnopqrstuvwxyz'):
    dic[alpha] = i
for s in string:
    num_of_alpha[dic[s]] += 1
for num in num_of_alpha:
    output += f'{num} '
print(output)

#10809
string = input()
num_of_alpha,dic,output = [-1]*26, {}, ''
for i,alpha in enumerate('abcdefghijklmnopqrstuvwxyz'):
    dic[alpha] = i
for i,s in enumerate(string):
    if(num_of_alpha[dic[s]] == -1):
        num_of_alpha[dic[s]] = i
for num in num_of_alpha:
    output += f'{num} '
print(output)


#10820 다시풀면 rstrip() stdout활용하자.
import sys
string = sys.stdin.readline()
while(string):
    lower,upper,digit,space = 0,0,0,0
    for s in string:
        if(s.islower()):
            lower += 1
        elif(s.isupper()):
            upper += 1
        elif(s.isdigit()):
            digit += 1
        elif(s == ' '):
            space += 1    
    print(f'{lower} {upper} {digit} {space}')
    string = ''
    string = sys.stdin.readline()


#2743
string = input()
print(len(string))

#11655
table = [['a', 'A'],
 ['b', 'B'],
 ['c', 'C'],
 ['d', 'D'],
 ['e', 'E'],
 ['f', 'F'],
 ['g', 'G'],
 ['h', 'H'],
 ['i', 'I'],
 ['j', 'J'],
 ['k', 'K'],
 ['l', 'L'],
 ['m', 'M'],
 ['n', 'N'],
 ['o', 'O'],
 ['p', 'P'],
 ['q', 'Q'],
 ['r', 'R'],
 ['s', 'S'],
 ['t', 'T'],
 ['u', 'U'],
 ['v', 'V'],
 ['w', 'W'],
 ['x', 'X'],
 ['y', 'Y'],
 ['z', 'Z']]
dic = {'a': 0,
 'A': 0,
 'b': 1,
 'B': 1,
 'c': 2,
 'C': 2,
 'd': 3,
 'D': 3,
 'e': 4,
 'E': 4,
 'f': 5,
 'F': 5,
 'g': 6,
 'G': 6,
 'h': 7,
 'H': 7,
 'i': 8,
 'I': 8,
 'j': 9,
 'J': 9,
 'k': 10,
 'K': 10,
 'l': 11,
 'L': 11,
 'm': 12,
 'M': 12,
 'n': 13,
 'N': 13,
 'o': 14,
 'O': 14,
 'p': 15,
 'P': 15,
 'q': 16,
 'Q': 16,
 'r': 17,
 'R': 17,
 's': 18,
 'S': 18,
 't': 19,
 'T': 19,
 'u': 20,
 'U': 20,
 'v': 21,
 'V': 21,
 'w': 22,
 'W': 22,
 'x': 23,
 'X': 23,
 'y': 24,
 'Y': 24,
 'z': 25,
 'Z': 25}
string = input()
output = ''
for s in string:
    if(s.isupper()):
        output += table[(dic[s]+13)%26][1]
    elif(s == ' ' or s.isdigit()):
        output += s
    else:
        output += table[(dic[s]+13)%26][0]
print(output)


#10824
nums = input().split()
print(int(nums[0]+nums[1])+int(nums[2]+nums[3]))

#11656
string = input()
subs = []
for i in range(len(string)):
    subs.append(string[i:])
subs.sort()
for sub in subs:
    print(sub)




#가희 알고리즘대
#1
#2n-1 : n에서 출발 2n: n+1도착
city = 'Seoul Yeongdeungpo Anyang Suwon Osan Seojeongri Pyeongtaek Seonghwan Cheonan Sojeongni Jeonui Jochiwon Bugang Sintanjin Daejeon Okcheon Iwon Jitan Simcheon Gakgye Yeongdong Hwanggan Chupungnyeong Gimcheon Gumi Sagok Yangmok Waegwan Sindong Daegu Dongdaegu Gyeongsan Namseonghyeon Cheongdo Sangdong Miryang Samnangjin Wondong Mulgeum Hwamyeong Gupo Sasang Busan'
d = '0.0 9.1 23.9 41.5 56.5 66.5 75.0 84.4 96.6 107.4 114.9 129.3 139.8 151.9 166.3 182.5 190.8 196.4 200.8 204.6 211.6 226.2 234.7 253.8 276.7 281.3 289.5 296.0 305.9 323.1 326.3 338.6 353.1 361.8 372.2 381.6 394.1 403.2 142.4 421.8 425.2 430.3 441.7'

dic = {'Seoul': 0.0,  'Yeongdeungpo': 9.1,  'Anyang': 23.9,  'Suwon': 41.5,  'Osan': 56.5,
 'Seojeongri': 66.5,  'Pyeongtaek': 75.0,  'Seonghwan': 84.4,  'Cheonan': 96.6,  'Sojeongni': 107.4,
 'Jeonui': 114.9,  'Jochiwon': 129.3,  'Bugang': 139.8,  'Sintanjin': 151.9,  'Daejeon': 166.3,
 'Okcheon': 182.5,  'Iwon': 190.8,  'Jitan': 196.4,  'Simcheon': 200.8,  'Gakgye': 204.6,
 'Yeongdong': 211.6,  'Hwanggan': 226.2,  'Chupungnyeong': 234.7,  'Gimcheon': 253.8,  'Gumi': 276.7,
 'Sagok': 281.3, 'Yangmok': 289.5,  'Waegwan': 296.0,  'Sindong': 305.9,  'Daegu': 323.1, 
 'Dongdaegu': 326.3,  'Gyeongsan': 338.6,  'Namseonghyeon': 353.1,  'Cheongdo': 361.8,  'Sangdong': 372.2,
 'Miryang': 381.6,  'Samnangjin': 394.1,  'Wondong': 403.2,  'Mulgeum': 142.4,  'Hwamyeong': 421.8,
 'Gupo': 425.2, 'Sasang': 430.3, 'Busan': 441.7}
city = ['Seoul',  'Yeongdeungpo',  'Anyang',  'Suwon',  'Osan',  'Seojeongri',  'Pyeongtaek',  'Seonghwan',
 'Cheonan',  'Sojeongni',  'Jeonui',  'Jochiwon',  'Bugang',  'Sintanjin',  'Daejeon',  'Okcheon',
 'Iwon',  'Jitan',  'Simcheon',  'Gakgye',  'Yeongdong',  'Hwanggan',  'Chupungnyeong',  'Gimcheon',
 'Gumi',  'Sagok',  'Yangmok',  'Waegwan',  'Sindong',  'Daegu',  'Dongdaegu',  'Gyeongsan',
 'Namseonghyeon',  'Cheongdo',  'Sangdong',  'Miryang',  'Samnangjin',  'Wondong',  'Mulgeum',  'Hwamyeong',
 'Gupo',  'Sasang',  'Busan']
# 서울에서 부산코스주고 부산에서 서울가는시간 계산하라고하면?
#dic_t의 첫도시와 끝도시 인덱스관계랑 질문의 첫도시와 끝도시 인덱스 관계가 같게설정하자.
N,Q = map(int,(input().split()))
dic_t,order = {},[]
for _ in range(N):
    c, e, s = input().split()
    dic_t[c] = [e,s]
for _ in range(Q):
    s,e = input().split()
    d = abs(dic[s] - dic[e])
    tsh,tsm = map(float,dic_t[s][1].split(':'))
    teh,tem = map(float,dic_t[e][0].split(':'))
    ts = tsh + tsm/60
    te = teh + tem/60
    if(ts>te):
        te+= 24
    t = (te - ts)
    print(d/t)

#sys.stdin.readline
import sys
N,Q = map(int,(sys.stdin.readline().split()))
dic_t = {}
for _ in range(N):
    c, e, s = sys.stdin.readline().split()
    dic_t[c] = [e,s]
for _ in range(Q):
    s,e = sys.stdin.readline().split()
    d = abs(dic[s] - dic[e])
    tsh,tsm = map(int,dic_t[s][1].split(':'))
    teh,tem = map(int,dic_t[e][0].split(':'))
    tsh = float(tsh + tsm/60)
    teh = float(teh + tem/60)
    if(tsh>teh):
        teh+= 24
    print(d/(teh-tsh))










#2
#a+b 사이의 건물을 a앞에다 1로 쭉둔다.
#차례대로 세우고 낮춘다.
N, a, b = map(int,input().split())
if(a+b < 2 or a+b > N+1):
    print(-1)
else:
    output = ''
    for _ in range(N-a-b+1):
        output += ('1 ')
    if(a>=b):
        for i in range(1,a+1):
            output += str(i)+ ' '
        for j in range(b-1,0,-1):
            output += str(j) + ' '
    else:
        for i in range(1,a):
            output += str(i)+ ' '    
        for j in range(b,0,-1):
            output += str(j) + ' '
    
    print(output[:-1])

N, a, b = map(int,input().split())
if(a+b < 2 or a+b > N+1):
    print(-1)
elif(a!=1):
    output = ''
    for _ in range(N-a-b+1):
        output += ('1 ')
    if(a>=b):
        for i in range(1,a+1):
            output += str(i)+ ' '    
        for j in range(b-1,0,-1):
            output += str(j) + ' '
    else:
        for i in range(1,a):
            output += str(i)+ ' '    
        for j in range(b,0,-1):
            output += str(j) + ' '    
    print(output[:-1])
else:
    output = str(b) + ' '
    for _ in range(N-a-b+1):
        output += ('1 ')
    for j in range(b-1,0,-1):
        output += str(j) + ' '
    print(output[:-1])


#a 가 1인경우!!!!!
#8 1 5









































































