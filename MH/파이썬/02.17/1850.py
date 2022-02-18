n,m = map(int,input().split())

while n!=0:
    m%=n
    n,m = m,n
print("1"*m)