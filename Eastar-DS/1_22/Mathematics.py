#Mathematics


#10430 print의 sep를 배웠다.
A,B,C = map(int,input().split())
print((A+B)%C, (A%C+B%C)%C, (A*B)%C, (A%C * B%C)%C, sep="\n")

#2609 유클리드 호제법
def GCD(x,y) :
    while(y):
        x,y = y,x%y
    return x
x,y =  map(int,input().split())
gcd = GCD(x,y)
print(gcd, x*y//gcd, sep="\n")

#1934
def GCD(x,y) :
    while(y):
        x,y = y,x%y
    return x
T = int(input())
for _ in range(T):
    x,y = map(int,input().split())
    gcd = GCD(x,y)
    print(x*y//gcd)

#1850
def GCD(x,y) :
    while(y):
        x,y = y,x%y
    return x
x,y =  map(int,input().split())
gcd = GCD(x,y)
print('1'*gcd)

#9613
def GCD(x,y) :
    while(y):
        x,y = y,x%y
    return x
t = int(input())
for _ in range(t):
    nums = list(map(int,input().split()))
    length,output = len(nums),0
    for i in range(1, length-1):
        for j in range(i+1,length):
            output += GCD(nums[i],nums[j])
    print(output)



#11005 divmod라는 함수가있네
over10 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, B = map(int, input().split())
new = ''
while(N>=B):
    r = N%B
    if(r>9):
        r = over10[r-10]
        new = r + new
    else:
        new = str(r) + new
    N //= B
if(N>9):
    new = over10[N-10] + new
else:
    new = str(N) + new
print(new)

#2745 int에 base넣어주면 바로해결이였넹~
dic = {'0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
       'A': 10,  'B': 11, 'C': 12,  'D': 13,  'E': 14,  'F': 15,  'G': 16,  'H': 17,  'I': 18,
 'J': 19,  'K': 20,  'L': 21,  'M': 22,  'N': 23,  'O': 24,  'P': 25,  'Q': 26,  'R': 27,
 'S': 28,  'T': 29,  'U': 30,  'V': 31,  'W': 32,  'X': 33,  'Y': 34,  'Z': 35}
N,B = input().split()
B = int(B)
output = 0
for i,digit in enumerate(N[::-1]):
    output += dic[digit]*B**i
print(output)

N,B = input().split()
print(int(N,int(B)))


#1373
N = input()
dic = {'000':'0','001':'1','010':'2', '011':'3', '100':'4', '101':'5', '110':'6', '111':'7'}
length,new = len(N),''
for i in range(length-1,1,-3):
    new = dic[N[i-2:i+1]] + new
if(length%3 == 1):
    new = dic['00'+N[0]] + new
elif(length%3 == 2):
    new = dic['0'+N[0:2]] + new
print(new)

#1등풀이 exit를 배웠다
N = input()

if N == '0':
    print(0)
    exit()

N = int(N, 2)

print(oct(N).replace('0o', ''))


#1212
n = input()
first = {'0':'0','1':'1','2':'10', '3':'11', '4':'100', '5':'101', '6':'110', '7':'111'}
dic = {'0':'000','1':'001','2':'010', '3':'011', '4':'100', '5':'101', '6':'110', '7':'111'}
length = len(n)
if(length == 1):
    print(first[n])
else:
    output = first[n[0]]
    for digit in n[1:]:
        output += dic[digit]
    print(output)


#2089 
n = int(input())
if(n == 0):
    print('0')
    exit()
output = ''
while(n):
    #나머지가 0이 아니면
    if(n%-2):
        output = '1' + output
        n = n//-2 + 1
    else:
        output = '0' + output
        n = n//-2
print(output)


import sys 
N = int(sys.stdin.readline()) 
if not N: 
    sys.stdout.write('0') 
    exit() 
res = '' 
while N: 
    if N%(-2): 
        res = '1' + res 
        N = N//-2 + 1 
    else: 
        res = '0' + res 
        N //= -2 
sys.stdout.write(res)

#11576
A,B = map(int,input().split())
length = input()
numA = list(map(int,input().split()))
num10 = 0
for i,num in enumerate(numA[::-1]):
    num10 += num*A**i
numB = []
while(num10):
    numB.append(num10%B)
    num10 //= B
print(' '.join([str(num) for num in numB[::-1]]))


#1978 x==2 안써서 시간낭비했
def isPrime(x):
    import math
    if(x == 2):
        return True
    if(x%2 == 0 or x == 1):
        return False
    for i in range(3,math.floor(math.sqrt(x)) + 1,2):
        if(x%i == 0):
            return False
    return True
N = int(input())
nums = list(map(int,input().split()))
prime = 0
for n in nums:
    if(isPrime(n)):
        prime += 1
print(prime)

#1929
def isPrime(x):
    import math
    if(x == 2):
        return True
    if(x%2 == 0 or x == 1):
        return False
    for i in range(3,math.floor(math.sqrt(x)) + 1,2):
        if(x%i == 0):
            return False
    return True
M,N = map(int,input().split())
for i in range(M,N+1):
    if isPrime(i):
        print(i)

#6588
def isPrime(x):
    import math
    if(x == 2):
        return True
    if(x%2 == 0 or x == 1):
        return False
    for i in range(3,math.floor(math.sqrt(x)) + 1,2):
        if(x%i == 0):
            return False
    return True
import sys
n = int(sys.stdin.readline())
while(n):
    for a in range(3,n//2 + 1,2):
        if(isPrime(a) and isPrime(n-a)):
            print(f'{n} = {a} + {n-a}')
            break
    n = int(sys.stdin.readline())
    
#11653
N = int(input())
while(N%2 == 0):
    print(2)
    N //= 2
i = 3
while(N != 1):
    if(N%i == 0):
        print(i)
        N //=i
    else:
        i += 2

#10872
N = int(input())
if(N == 0 or N == 1):
    print(1)
else:
    output = 1
    for i in range(2,N+1):
        output *= i
    print(output)

#1676
n = int(input())
output = 0
for i in [5,25,125]:
    output += (n//i)
print(output)

#2004
def num2(n):
    a,out = 2,0
    while(a<=n):
        out += n//a
        a *= 2
    return out
def num5(n):
    a,out = 5,0
    while(a<=n):
        out += n//a
        a *= 5
    return out
n,m = map(int,input().split())
print(min(num2(n)-num2(m)-num2(n-m),num5(n)-num5(m)-num5(n-m)))



















