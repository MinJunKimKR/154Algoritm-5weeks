n = int(input())
arr = list(map(int,input().split()))
arr.sort()

sum = 0
tmp = 0
for i in arr:
    tmp += i
    sum+=tmp
print(sum)