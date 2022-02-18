n = int(input())
arr = [i for i in range(1,n+1)]

ans=1
for i in arr:
     ans*=i
ans = str(ans)

num=0
for i in reversed(ans):
    if i!="0":
        break
    else:
        num+=1

print(num)