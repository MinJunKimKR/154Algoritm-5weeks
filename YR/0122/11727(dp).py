#11726 문제의 응용.
#2*2블록도 사용가능하므로 d[i-2]경우에 2를 곱해준다.

d=[0]*1001
d[1]=1
d[2]=2


n=int(input())
for i in range(3,n+1):
    d[i]=2*d[i-2]+d[i-1]
print(d[n]%10007)

