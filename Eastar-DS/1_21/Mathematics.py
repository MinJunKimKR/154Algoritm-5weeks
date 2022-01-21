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











































