tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n,b = input().split()
arr = []

for i in n:
    arr.append(tmp.index(i))

ans = int(arr[0])
for i in range(1,len(arr)):
    ans = ans*int(b)+arr[i]

print(ans)

