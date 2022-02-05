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
