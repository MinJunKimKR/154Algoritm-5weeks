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























