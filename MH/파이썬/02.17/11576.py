a,b = map(int,input().split())
n = int(input())
arr = list(map(int,input().split()))
ans = []
ten = 0

for i in range(n):
    ten+=arr[-1]*(a**i)
    arr.pop(-1)
    print(ten)

while ten != 0:
    ans.append(str(ten%b))
    ten = ten//b

print(" ".join(ans[::-1]))
