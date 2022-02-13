#1107
#골드5
import sys
input=sys.stdin.readline
num=input()

n=int(input())

arr=list(map(int,input().split()))

min_count=abs(100-int(num)) # +, - 버튼만을 가지고 움직일 경우.
for i in range(1000001):
    st=str(i)

    for j in range(len(st)):
        if int(st[j]) in arr: #고장난 버튼이 있다면
            break

        #고장난숫자가 없다면
        elif j==len(st)-1:
            min_count=min(min_count,abs(i-int(num))+len(st))

print(min_count)

#마지막 케이스 같은 경우때문에 일일이 따져봐야할듯.



