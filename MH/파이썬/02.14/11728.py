a,b = map(int,input().split())
alist = list(map(int,input().split()))
blist = list(map(int,input().split()))

ans = alist+blist
ans.sort()
print(*ans)