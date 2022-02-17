import sys
input = sys.stdin.readline

arr = [True]*(1000001)
for i in range(2,int(1000000**0.5)+1):
    if arr[i]:
        for j in range(i*2,1000000+1,i):
            arr[j] = False


while True:
    n = int(input())
    check = False
    a,b = 0,0
    if n == 0:
        break
    for i in range(3,1000001):
        if arr[i]:
            if arr[n-i]:
                a,b = i,n-i
                check = True
                break

    if check:
        print("{} = {} + {}".format(n,a,b))
    else:
        print("Goldbach's conjecture is wrong.")
