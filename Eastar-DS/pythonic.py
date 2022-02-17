#알고리즘 이용할것들

#90도 회전
def rotate(arr):
    return list(zip(*arr[::-1]))

print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# [(7, 4, 1)
# (8, 5, 2)
# (9, 6, 3)]


#2609 최대공약수 유클리드 호제법
def GCD(x,y) :
    while(y):
        x,y = y,x%y
    return x


#소수판별
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


#에라토스테네스의 체
def primes(N):
    import math
    if(N == 1):
        return []
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
    return primes


# if else문 두번째 for문 안에 첫번째 for문의 인자를 사용해야 else가 제대로 작동하는듯.
for i in range(12):
    for s in str(i):
        if '1' in s:
            break
    else:
        print(i)


#global을 이용하면 함수안에서 바깥의 변수사용가능
test = 0
def testFtn():
    global test
    test += 3
testFtn()
print(test)


#List Comprehension
#if, else를 쓰고싶으면 앞쪽에.
[int(s) if s != ' ' else 0 for s in '1 2 3']
#if만쓰고싶으면 뒤쪽에.
[int(s) for s in '1 2 3' if s != ' ']













