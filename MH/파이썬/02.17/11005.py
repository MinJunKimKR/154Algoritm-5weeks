tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n,b = map(int,input().split())
answer=""

while n != 0:
    answer+=str(tmp[n%b])
    n = n//b

print(answer[::-1])
